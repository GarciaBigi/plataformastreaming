import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
def frame_ingreso(root,autenticacion):
    f=Frame(root)
    f.configure(bg = "#292F36")
    bienvenida = Label(f, text="Bienvenido a esta plataforma, por favor ingrese su correo y contraseña", background = "#FFFFFF")
    bienvenida.grid(row=1,column=1,padx=10)

    correo = Text(f, height=2,width=30, background = "#FFFFFF")
    correo.grid(row=4, column=1)

    contraseña = Text(f, height=2,width=30, background="#FFFFFF")
    contraseña.grid(row=6,column=1)

    botonIngresar = Button(f, text="Ingresar", command= lambda: autenticacion(correo.get("1.0", "end-1c"), contraseña.get("1.0","end-1c")),background="#FFFFFF", relief="raised",borderwidth=4)
    botonIngresar.grid(row=5, column=3)
    return f
def frame_perfiles(root):
    f=Frame(root)
    f.configure(bg = "#292F36")

    bienvenidaPerfiles = Label(f,text="Bienvenido, seleccione un perfil", background="#493548")
    bienvenidaPerfiles.grid(row=1,column=1,padx=10)

    return f