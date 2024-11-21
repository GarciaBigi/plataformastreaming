import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def frame_ingreso(root, autenticacion,*,creacion=None, cambiocontra=None, nuevacreacion=False, nuevacontrasena=(False,"")):
    f = Frame(root, bg="#FFFFFF", width=450, height=450)
    f.grid_propagate(False)
    
    Label(f,text="Bienvenido a esta plataforma.\nPor favor, ingrese su correo y contraseña.",bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").grid(row=0, column=0, columnspan=2, pady=20, padx=10)
    
    Label(f, text="Correo electrónico:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=1, column=0, pady=10, sticky="e")
    correo = Entry(f, width=30, bg="#F7F7F7", bd=1, relief="solid")
    correo.grid(row=1, column=1, pady=10, padx=10)
    
    Label(f, text="Contraseña:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=2, column=0, pady=10, sticky="e")
    contraseña = Entry(f, show="*", width=30, bg="#F7F7F7", bd=1, relief="solid")
    contraseña.grid(row=2, column=1, pady=10, padx=10)
    
    Button(f, text="Ingresar", command=lambda: autenticacion(correo.get(), contraseña.get()),bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="flat", width=15, height=1).grid(row=3, column=1, pady=20)
    
    if nuevacreacion:
        Button(f, text="¿Crear nueva cuenta?", command=creacion,bg="#FFFFFF", fg="#4CAF50", font=("Arial", 10, "underline"), relief="flat").grid(row=4, column=1, pady=10)
    if nuevacontrasena[0]:
        Button(f, text="¿Olvidaste la contraseña?", command=lambda: cambiocontra(nuevacontrasena[1]),bg="#FFFFFF", fg="#4CAF50", font=("Arial", 10, "underline"), relief="flat").grid(row=5, column=1, pady=10)
    return f


def frame_perfiles(root, listaPer,servicio):
    f = Frame(root, bg="#FFFFFF", width=450, height=450)
    f.grid_propagate(False)
    
    Label(f, text="Bienvenido, seleccione un perfil.",bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=20)
    
    canvas = Canvas(f, bg="#FFFFFF", highlightthickness=0, width=430, height=300)
    scrollbar = Scrollbar(f, orient="vertical", command=canvas.yview)
    profiles_frame = Frame(canvas, bg="#FFFFFF")
    
    for i, perfil in enumerate(listaPer):
        Label(profiles_frame, text=f"{perfil[0]}", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        Button(profiles_frame, text="Ingresar", command=lambda p=perfil[0]: servicio(p),bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10), relief="flat", width=10).grid(row=i, column=1, padx=10, pady=5)
    
    profiles_frame.update_idletasks()
    canvas.create_window(0, 0, anchor="nw", window=profiles_frame)
    canvas.update_idletasks()
    canvas.configure(yscrollcommand=scrollbar.set, scrollregion=canvas.bbox("all"))
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    return f




def frame_nuevacuenta(root, verificar):
    f = Frame(root, bg="#FFFFFF", width=450, height=450)
    f.grid_propagate(False)
    
    Label(f, text="Creación de una nueva cuenta",bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").grid(row=0, column=0, columnspan=2, pady=20, padx=10)
    
    Label(f, text="Ingrese nuevo correo:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=1, column=0, pady=10, sticky="e")
    nuevoUsuario = Entry(f, width=30, bg="#F7F7F7", bd=1, relief="solid")
    nuevoUsuario.grid(row=1, column=1, pady=10, padx=10)
    
    Label(f, text="Ingrese nueva contraseña:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=2, column=0, pady=10, sticky="e")
    nuevaContra1 = Entry(f, show="*", width=30, bg="#F7F7F7", bd=1, relief="solid")
    nuevaContra1.grid(row=2, column=1, pady=10, padx=10)
    
    Label(f, text="Repita nueva contraseña:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=3, column=0, pady=10, sticky="e")
    nuevaContra2 = Entry(f, show="*", width=30, bg="#F7F7F7", bd=1, relief="solid")
    nuevaContra2.grid(row=3, column=1, pady=10, padx=10)
    
    Button(f, text="Crear Cuenta", command=lambda: verificar(nuevoUsuario.get(), nuevaContra1.get()),bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="flat", width=15).grid(row=4, column=0, columnspan=2, pady=20)
    
    return f

def frame_nuevacontra(root, usuario, nuevacontra):
    f = Frame(root, bg="#FFFFFF", width=450, height=450)
    f.grid_propagate(False)

    Label(f, text=f"Bienvenido: {usuario}",bg="#FFFFFF", fg="#000000", font=("Arial", 14, "bold"),wraplength=400, justify="center").grid(row=0, column=0, columnspan=2, pady=20, padx=10)
    Label(f, text="Por favor, ingrese su nueva contraseña.",bg="#FFFFFF", fg="#555555", font=("Arial", 11),wraplength=400, justify="center").grid(row=1, column=0, columnspan=2, pady=10, padx=10)


    Label(f, text="Nueva contraseña:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=2, column=0, pady=10, sticky="e", padx=10)
    nuevaContra1 = Entry(f, show="*", width=30, bg="#F7F7F7", bd=1, relief="solid")
    nuevaContra1.grid(row=2, column=1, pady=10, padx=10)

    Label(f, text="Repita nueva contraseña:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=3, column=0, pady=10, sticky="e", padx=10)
    nuevaContra2 = Entry(f, show="*", width=30, bg="#F7F7F7", bd=1, relief="solid")
    nuevaContra2.grid(row=3, column=1, pady=10, padx=10)

    Button(f, text="Confirmar", command=lambda: nuevacontra(usuario,nuevaContra1.get(),),bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"),relief="flat", width=15, height=1).grid(row=4, column=0, columnspan=2, pady=20)

    return f


def frame_plataforma(root, perfil):
    f = Frame(root, bg="#FFFFFF", width=450, height=450)
    f.grid_propagate(False)
    Label(f, text=f"Bienvenido: {perfil}", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").grid(row=0, column=1, columnspan=2, pady=20, padx=10)
    Label(f, text="Continuar viendo", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=200, justify="center").grid(row=1, column=0, pady=20, padx=10, sticky="n")
    Label(f, text="Novedades", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=200, justify="center").grid(row=1, column=2, pady=20, padx=10, sticky="n")

    f.pack(fill="both", expand=True)
    
    return f
