import mysql.connector
from utils.consultas import * 
from utils.frames import *
import tkinter as tk

#Usuario y perfil actual(variables globales)
usuario_actual_id = None
perfil_actual_id= None
def set_usuario_actual(usuario_id):
    global usuario_actual_id
    usuario_actual_id = usuario_id
def set_perfil_actual(perfil):
    global perfil_actual_id  
    perfil_actual_id = perfil

#CAMBIAR FRAMES
def mostrar_frame(frame):
    global frameactual
    if frameactual is not None:
        frameactual.destroy()
    frameactual = frame
    frameactual.pack(fill="both", expand=True)
#PRIMER FRAME, es el frame donde se ingresa el usuario y contraseña
def autenticacion(correo, contraseña):
    if cnx.is_connected():
        cursor = cnx.cursor()
        try:
            usuarios = con_usuarios(cursor, correo) #Consulta a la base de datos por los datos ingresador
            if len(usuarios) == 0: #Caso donde no existe un usuario con ese correo
                frame = frame_ingreso(root, autenticacion, creacion=creacion, nuevacreacion=True) # Mostramos el cartel para que se pueda crear una cuenta con el atributo nuevacreacion=true
                mostrar_frame(frame)
            elif len(usuarios) == 1: #Ingreso exitoso, el suaurio y contraseña son correctos
                if usuarios[0][2] == contraseña:
                    ins_intento(cursor, True, usuarios[0][0]) #Se updatea el ingreso exitoso
                    cnx.commit()
                    set_usuario_actual(usuarios[0][0]) #Seteo la variable global
                    listaPer = obtener_perfiles(usuarios[0][0])
                    frame = frame_perfiles(root, listaPer, servicio, crearPerfil= crearPerfil)
                    mostrar_frame(frame)
                else:#Ingreso incorrencto, el usuario existe en la base de datos pero no con esa contraseña
                    ins_intento(cursor, False, usuarios[0][0]) #Se updatea el ingreso fallido
                    frame = frame_ingreso(root, autenticacion, cambiocontra=cambiarcontra, nuevacontrasena=(True,correo)) #Mostramos el cartel para que pueda cambiar su contraseña en caso que se haya olvidado, esto llama al frame con el atributo nuevacontrasena=true y su correo
                    mostrar_frame(frame)
                    cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()      
#PARA NUEVA CREACION DE Usuarios
def creacion():#Función la cual llama el boton para crear un nuevo usuario
    frame=frame_nuevacuenta(root,verificacion) 
    mostrar_frame(frame)

def verificacion(nuevoUsuario,nuevoContra):
    try:
        cursor=cnx.cursor()
        insert_usuario(cursor,nuevoUsuario,nuevoContra)#Se inserta el nuevo usuario y contraseña
        cnx.commit()
        frame=frame_ingreso(root,autenticacion) #Se vuelve al frame para que pueda ingresar
        mostrar_frame(frame)
    except mysql.connector.Error as err:
        cnx.rollback()
        print(f"Error: {err}")
    finally:
        cursor.close()

#PARA UPDATEAR CONTRASEÑA
def cambiarcontra(usuario):#Función la cual llama el boton para cambiar la contraseña, este cambia al frame_nuevacontra
    frame=frame_nuevacontra(root,usuario,nuevacontra)
    mostrar_frame(frame)

def nuevacontra(usuario, contrasena):
    try:
        cursor=cnx.cursor()
        upd_contrasena(cursor,usuario,contrasena) #Update de la contraseña en la base de datos
        cnx.commit()
        frame=frame_ingreso(root,autenticacion) #Volvemos al frame para que pueda ingresar
        mostrar_frame(frame)
    except mysql.connector.Error as err:
        cnx.rollback()
        print(f"Error: {err}")
    finally:
        cursor.close()

#MOSTRAR PERFILES
def obtener_perfiles(idUsuario):
    if cnx.is_connected:
        cursor=cnx.cursor()
        try:
            listaPerfiles = con_perfiles(cursor, idUsuario)#Se obtiene una lista con todos los perfiles asociados al id del usuario
            return listaPerfiles
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()
#CREAR PERFIL
def crearPerfil(nombre,tipo,id,servicio):
    if cnx.is_connected:
        cursor = cnx.cursor()
        try:
            insert_perfil(cursor, nombre, tipo, id)#Se agrega el nuevo perfil asociado al id del usuario
            cnx.commit()
            listaPer = obtener_perfiles(id)#Se obtiene la nueva lista de perfiles
            frame = frame_perfiles(root, listaPer, servicio, crearPerfil= crearPerfil)#Se vuelve a cargar el frame con el nuevo perfil
            mostrar_frame(frame)
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
            set_perfil_actual(perfil[1]) #Seteo el perfil actual de manera global
            listaContinuar = continuar_viendo(cursor, perfil[1])#Se consulta sobre los continuar viendo y novedades relacionadas a ese perfil
            if perfil[2] == True:
                listaNovedades = novedadesFil(cursor,perfil[2])#Si el perfil es infantil mostrara novedades que sean atp
            else:
                listaNovedades = novedades(cursor)#Si no es infantil muestra todas las novedades
            frame=frame_plataforma(root, listaContinuar,listaNovedades, perfil[2], busq=busq, vermultimedia=vermultimedia)#Se crea el frame de acurdo a los resultados de las consultas
            mostrar_frame(frame)
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()
#BUSQUEDA DE UN TITULO
def busq(texto, TipoPer):
    if cnx.is_connected:
        cursor=cnx.cursor()
        try:
            if TipoPer == False:
                listaBusqueda = buscarTitulo(cursor, texto)#Si el tipo de perfil es adulto realiza una busqueda sin filtros de edad
            else:
                listaBusqueda = buscarTituloFil(cursor, texto, TipoPer)#Si es infantil realiza una busqueda filtrada
            return listaBusqueda
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()

#Multimedias especificas
def vermultimedia(titulo):#Esta función busca el resumen de datos sobre una multimedia especifica, mostrando todos sus atributos y los artistas en su equipo de producción en un nuevo frame
    if cnx.is_connected:
        cursor=cnx.cursor()
        try:
            id = con_idmultimedia(cursor, titulo) #Se consulta el id de la multimedia
            multimedia= con_multimediafull(cursor,id) # En base a ese id se ve todos sus datos
            equipo= con_equipo(cursor,id)#Tambien se verifica todo el equipo de producción
            relacion=con_vistoycalif(cursor,perfil_actual_id,id)#Y se consulta con la variable global que calificacion y porcentaje visto tiene ese perfil para esa multimedia
            if len(relacion)!=0:#Este if previene errores en caso de seleccionar multimedias que todavia no visualizo ese perfil nunca
                visto=relacion[0][0]
                calif=relacion[0][1]
            else:
                visto="0"
                calif="0"
            frame=frame_multimedia(root,visto=visto,calificacion=calif,mirarmultimedia=mirar_multimedia,multimedia=multimedia,equipo=equipo)
            mostrar_frame(frame)
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()

def mirar_multimedia(titulo,vista,calif,firstime):#Función para updatear el porcentaje visto y la calificacion personal de esa multimedia
    if cnx.is_connected:
        cursor=cnx.cursor()
        try:
            id_multimedia = con_idmultimedia(cursor, titulo)
            id_perfil = perfil_actual_id
            if firstime: #Si es la primera ocasion qie mira esa multimedia se hara un insert
                ins_mirar(cursor,id_multimedia,id_perfil,vista,calif)
                cnx.commit()
            else:#Si por otro lado ya la habia visto se realizara un update
                upd_mirar(cursor,id_multimedia,id_perfil,vista,calif)
                cnx.commit()
            multimedia= con_multimediafull(cursor,id_multimedia) 
            equipo= con_equipo(cursor,id_multimedia)
            frame=frame_multimedia(root,visto=vista,calificacion=calif,mirarmultimedia=mirar_multimedia,multimedia=multimedia,equipo=equipo)
            mostrar_frame(frame)
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()




#############COMIENZA CODIGO###########################################################################################
def ir_cambiar_usuario(): #Funcion para cambiar el usuario/cerrar sesión
    global usuario_actual_id
    usuario_actual_id = None
    frame = frame_ingreso(root, autenticacion)
    mostrar_frame(frame)

def ir_elegir_perfil():#Funcion para ir a elegir perfiles
    global usuario_actual_id
    if usuario_actual_id is not None:
        try:
            cursor = cnx.cursor()
            listaPer = obtener_perfiles(usuario_actual_id)#obtiene todos los perfiles asociados al id del usuario
            frame = frame_perfiles(root, listaPer, servicio)#invoca el frame para mostrar los perfiles
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

##### Menú principal
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

menu_opciones = tk.Menu(menu_bar, tearoff=0)
menu_opciones.add_command(label="Cerrar sesión", command=ir_cambiar_usuario)
menu_opciones.add_command(label="Cambiar perfil", command=ir_elegir_perfil)

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