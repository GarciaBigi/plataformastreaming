import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
def frame_ingreso(root,autenticacion,creacion=None,nuevacreacion=False):
    f=Frame(root)
    f.configure(bg = "#292F36")
    bienvenida = Label(f, text="Bienvenido a esta plataforma, por favor ingrese su correo y contraseña", background = "#FFFFFF")
    bienvenida.grid(row=1,column=1,padx=10)

    correo = Text(f, height=2,width=30, background = "#FFFFFF")
    correo.grid(row=4, column=1)

    contraseña = Text(f, height=2,width=30, background="#FFFFFF")
    contraseña.grid(row=6,column=1)

    botonIngresar = Button(f, text="Ingresar", command= lambda: autenticacion(correo.get("1.0", "end-1c"), contraseña.get("1.0","end-1c")),background="#FFFFFF", relief="raised",borderwidth=4)
    botonIngresar.grid(row=5, column=2)
    if nuevacreacion:
        botonNueva= Button(f, text="¿Quiere crear una nueva cuenta?", command=creacion ,background="#FFFFFF", relief="raised",borderwidth=4)
        botonNueva.grid(row=4, column=2)
    return f
def frame_perfiles(root,listaPer):
    f=Frame(root)
    f.configure(bg = "#292F36")

    bienvenidaPerfiles = Label(f,text="Bienvenido, seleccione un perfil", background="#493548")
    bienvenidaPerfiles.grid(row=1,column=1,padx=10)

    for i in range(len(listaPer)):
        perfil = Label(f,text=f"{listaPer[i][0]}", background="#493548")
        perfil.grid(row=i+1, column=2, padx=10)
        Ingresar = Button(f,text="Ingresar", command= lambda : print("Ingresando"), background="#FFFFFF", relief="raised",borderwidth=4)
        Ingresar.grid(row=i+1,column=4)
    

    return f

def frame_nuevacuenta(root,verificar):
    f=Frame(root)
    f.configure(bg = "#292F36")

    cartel= Label(f, text="Creación de una nueva cuenta",background = "#FFFFFF")
    cartel.grid(row=1, column=1)

    cartel2= Label(f, text="Ingrese nuevo mail",background = "#FFFFFF")
    cartel2.grid(row=3, column=1)

    nuevoUsuario= Text(f, height=2,width=30, background="#FFFFFF")
    nuevoUsuario.grid(row=3, column=2)

    cartel3= Label(f, text="Ingrese nueva contraseña",background = "#FFFFFF")
    cartel3.grid(row=4,column=1)

    nuevaContra1= Text(f, height=2,width=30, background="#FFFFFF")
    nuevaContra1.grid(row=4, column=2)

    cartel4= Label(f, text="Repita nueva contraseña",background = "#FFFFFF")
    cartel4.grid(row=5,column=1)

    nuevaContra2= Text(f, height=2,width=30, background="#FFFFFF")
    nuevaContra2.grid(row=5, column=2)

    boton=  Button(f, text="CREAR", command= lambda: verificar(nuevoUsuario.get("1.0","end-1c"),nuevaContra1.get("1.0", "end-1c")),background="#FFFFFF", relief="raised",borderwidth=4)
    boton.grid(row=6,column=3)
    
    return f

