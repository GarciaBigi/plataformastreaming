import mysql.connector
from utils.consultas import * 
from utils.frames import *
import tkinter as tk
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


def obtener_perfiles(idUsuario):
    if cnx.is_connected:
        cursor=cnx.cursor()
        try:
            listaPerfiles = con_perfiles(cursor, idUsuario)
            print(listaPerfiles)
            return listaPerfiles
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()


def creacion():
    frame=frame_nuevacuenta(root,verificacion)
    mostrar_frame(frame)

def autenticacion(correo, contraseña):
    if cnx.is_connected():
        cursor=cnx.cursor()
        print(correo)
        try:
            usuarios=con_usuarios(cursor, correo)
            print(usuarios)
            if len(usuarios)==0:
                print("No existe un usuario con ese correo")
                frame = frame_ingreso(root, autenticacion,creacion, True)
                mostrar_frame(frame)
            elif len(usuarios)==1:
                if usuarios[0][2]==contraseña:
                    print("Correcto")
                    ins_intento(cursor,True,usuarios[0][0])
                    cnx.commit()
                    listaPer = obtener_perfiles(usuarios[0][0])
                    frame = frame_perfiles(root,listaPer)
                    mostrar_frame(frame)
                else:
                    print("Incorrecto")
                    ins_intento(cursor,False,usuarios[0][0])
                    cnx.commit()
        except mysql.connector.Error as err:
            cnx.rollback()
            print(f"Error: {err}")
        finally:
            cursor.close()
    




def mostrar_frame(frame):
    """Cambia al frame dado."""
    global frameactual
    if frameactual is not None:
        frameactual.destroy()
    frameactual = frame
    frameactual.pack(fill="both", expand=True)

#Ventana principal
root=tk.Tk()
root.title("Plataforma Streaming")
root.geometry("850x400")
frameactual=None
root.configure(bg = "#292F36")

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