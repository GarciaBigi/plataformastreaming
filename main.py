import mysql.connector
from utils.consultas import * 
from utils.frames import *
import tkinter as tk

usuario_actual_id = None
def set_usuario_actual(usuario_id):
    global usuario_actual_id
    usuario_actual_id = usuario_id

#CAMBIAR FRAMES
def mostrar_frame(frame):
    global frameactual
    if frameactual is not None:
        frameactual.destroy()
    frameactual = frame
    frameactual.pack(fill="both", expand=True)
#PRIMER FRAME
def autenticacion(correo, contraseña):
    if cnx.is_connected():
        cursor = cnx.cursor()
        try:
            usuarios = con_usuarios(cursor, correo)
            if len(usuarios) == 0:
                print("No existe un usuario con ese correo")
                frame = frame_ingreso(root, autenticacion, creacion=creacion, nuevacreacion=True)
                mostrar_frame(frame)
            elif len(usuarios) == 1:
                if usuarios[0][2] == contraseña:
                    print("Correcto")
                    ins_intento(cursor, True, usuarios[0][0])
                    cnx.commit()
                    set_usuario_actual(usuarios[0][0])
                    listaPer = obtener_perfiles(usuarios[0][0])
                    frame = frame_perfiles(root, listaPer, servicio, crearPerfil= crearPerfil)
                    mostrar_frame(frame)
                else:
                    print("Incorrecto")
                    ins_intento(cursor, False, usuarios[0][0])
                    frame = frame_ingreso(root, autenticacion, cambiocontra=cambiarcontra, nuevacontrasena=(True,correo))
                    mostrar_frame(frame)
                    cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()      
#PARA NUEVA CREACION DE Usuarios
def creacion():
    frame=frame_nuevacuenta(root,verificacion)
    mostrar_frame(frame)

def verificacion(nuevoUsuario,nuevoContra):
    try:
        cursor=cnx.cursor()
        insert_usuario(cursor,nuevoUsuario,nuevoContra)
        cnx.commit()
        frame=frame_ingreso(root,autenticacion)
        mostrar_frame(frame)
    except mysql.connector.Error as err:
        cnx.rollback()
        print(f"Error: {err}")
    finally:
        cursor.close()
#PARA UPDATEAR CONTRASEÑA
def nuevacontra(usuario, contrasena):
    try:
        cursor=cnx.cursor()
        upd_contrasena(cursor,usuario,contrasena)
        cnx.commit()
        frame=frame_ingreso(root,autenticacion)
        mostrar_frame(frame)
    except mysql.connector.Error as err:
        cnx.rollback()
        print(f"Error: {err}")
    finally:
        cursor.close()

def cambiarcontra(usuario):
    print(usuario)
    frame=frame_nuevacontra(root,usuario,nuevacontra)
    mostrar_frame(frame)

#MOSTRAR PERFILES
def obtener_perfiles(idUsuario):
    if cnx.is_connected:
        cursor=cnx.cursor()
        try:
            listaPerfiles = con_perfiles(cursor, idUsuario)
            return listaPerfiles
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()

def crearPerfil(nombre,tipo,id):
    if cnx.is_connected:
        cursor = cnx.cursor()
        try:
            insert_perfil(cursor, nombre, tipo, id)
            cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()

#PLATAFORMA STREAMING
def servicio(perfil):
    if cnx.is_connected():
        cursor=cnx.cursor()
        try: 
            listaContinuar = continuar_viendo(cursor, perfil[1])
            if perfil[2] == True:
                listaNovedades = novedadesFil(cursor,perfil[2])
            else:
                listaNovedades = novedades(cursor)
            
            frame=frame_plataforma(root, listaContinuar,listaNovedades, perfil[2], busq=busq, vermultimedia=vermultimedia)
            mostrar_frame(frame)
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()

def busq(texto, TipoPer):
    if cnx.is_connected:
        cursor=cnx.cursor()
        try:
            if TipoPer == False:
                listaBusqueda = buscarTitulo(cursor, texto)
            else:
                listaBusqueda = buscarTituloFil(cursor, texto, TipoPer)
            return listaBusqueda
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()

#Multimedias especificas
def vermultimedia(titulo):
    if cnx.is_connected:
        cursor=cnx.cursor()
        try:
            print(titulo)
            id = con_idmultimedia(cursor, titulo)
            multimedia= con_multimediafull(cursor,id)
            equipo= con_equipo(cursor,id)
            frame=frame_multimedia(root,multimedia=multimedia,equipo=equipo)
            mostrar_frame(frame)
            print(id)
            print(multimedia)
            print(equipo)
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()


#############COMIENZA CODIGO###########################################################################################
def ir_cambiar_usuario():
    global usuario_actual_id
    usuario_actual_id = None
    frame = frame_ingreso(root, autenticacion)
    mostrar_frame(frame)

def ir_elegir_perfil():
    global usuario_actual_id
    if usuario_actual_id is not None:
        try:
            cursor = cnx.cursor()
            listaPer = obtener_perfiles(usuario_actual_id)
            frame = frame_perfiles(root, listaPer, servicio)
            mostrar_frame(frame)
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()
    else:
        print("Error: No se ha establecido un usuario actual.")
#Ventana principal
root=tk.Tk()
root.title("Plataforma Streaming")
root.geometry("450x700")
frameactual=None
root.configure(bg = "#292F36")

# Menú principal
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_opciones = tk.Menu(menu_bar, tearoff=0)
menu_opciones.add_command(label="Cambiar Usuario", command=ir_cambiar_usuario)
menu_opciones.add_command(label="Elegir Perfil", command=ir_elegir_perfil)

menu_bar.add_cascade(label="Opciones", menu=menu_opciones)

# Datos de conexión a la base de datos
config = {
 "user": "root",
 "password": "",
 "host": "localhost",
 "database": "proyecto_pc2"
}

# Crea la conexión a la base de datos
cnx = mysql.connector.connect(**config)
print("Conectado:", cnx.is_connected())

# Mostrar el frame inicial
frame_ing = frame_ingreso(root, autenticacion)
mostrar_frame(frame_ing)


root.mainloop()
cnx.close()