import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


def frame_ingreso(root, autenticacion,*,creacion=None, cambiocontra=None, nuevacreacion=False, nuevacontrasena=(False,"")):
    f = Frame(root, bg="#FFFFFF", width=450, height=450)
    f.grid_propagate(False)
    
    Label(f,text="Bienvenido a esta plataforma.\nPor favor, ingrese su correo y contraseña.",bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").grid(row=0, column=0, columnspan=2, pady=20, padx=10)
    
    Label(f, text="Correo electrónico:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=1, column=0, pady=10, sticky="e")
    correo = Entry(f,width=30, bg="#F7F7F7", bd=1, relief="solid")
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
        Button(profiles_frame, text="Ingresar", command=lambda p=perfil: servicio(p),bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10), relief="flat", width=10).grid(row=i, column=1, padx=10, pady=5)
    
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

def frame_plataforma(root, listaContinuar, listaNovedades, *,busq = ""):
    f = Frame(root, bg="#FFFFFF", width=450, height=450)
    f.grid_propagate(False)

    # Título principal
    titulo = Label(f,text="Bienvenido a la plataforma",bg="#FFFFFF",fg="#000000",font=("Arial", 12, "bold"),wraplength=400,justify="center",)
    titulo.grid(row=0, column=0, columnspan=2, pady=10)
    #Buscador

    def callback(event):
        seleccion = listaBus.curselection()
        if seleccion:
            indice = seleccion[0]
            valor = listaBus.get(indice)
            print(valor)

    def obtener_resultados(texto):
        listaBus.delete(0,END)
        resultados = busq(texto)
        for elem in resultados:
            listaBus.insert(END, elem[1])
        listaBus.bind('<<ListboxSelect>>', callback)
        listaBus.config(height=min(len(resultados), 10))
        

    busqueda = Entry(f, width=40, bg="#F7F7F7", bd=1, relief="solid")
    busqueda.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    botonBuscar = Button(f, text= "Buscar", command= lambda: obtener_resultados(busqueda.get()), bg="#2A2D43", fg= "#000000" ,font=("Arial", 10),relief="flat", width=8)
    botonBuscar.grid(row=1, column=1, padx=5, pady=10, sticky="e")

    #listbox con scrollbar
    frame_listbox = Frame(f,bg="#FFFFFF")
    frame_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

    listaBus = Listbox(frame_listbox, width=40, height=10, bg="#F7F7F7", bd=1, relief="solid")
    listaBus.pack(side="left", fill="both", expand=True)

    scrollbarList = Scrollbar(frame_listbox, orient="vertical", command=listaBus.yview)
    scrollbarList.pack(side="right", fill="y")
    listaBus.config(yscrollcommand=scrollbarList.set)

    # Sección "Continuar viendo"
    Label(f,text="Continuar viendo",bg="#FFFFFF",fg="#000000",font=("Arial", 12, "bold"),wraplength=400,justify="center",).grid(row=3, column=0, columnspan=2, pady=5)

    frame_continuar = Frame(f, bg="#FFFFFF", width=450, height=100)
    frame_continuar.grid(row=4, column=0, columnspan=2, pady=5)
    
    canvas_continuar = Canvas(frame_continuar, bg="#FFFFFF", width=450, height=150, highlightthickness=0)
    scrollbar_continuar = Scrollbar(frame_continuar, orient="horizontal", command=canvas_continuar.xview)
    content_continuar = Frame(canvas_continuar, bg="#FFFFFF")

    canvas_continuar.configure(xscrollcommand=scrollbar_continuar.set)
    canvas_continuar.pack(side="top", fill="both", expand=True)
    scrollbar_continuar.pack(side="bottom", fill="x")

    canvas_continuar.create_window((0, 0), window=content_continuar, anchor="nw")

    for elem in listaContinuar:
        item_frame = Frame(content_continuar, bg="#FFFFFF")
        item_frame.pack(side="left", padx=10, pady=5)

        Label(item_frame, text=f"Titulo: {elem[1]}, Visto: {elem[2]}", bg="#FFFFFF", fg="#000000", font=("Arial", 10), wraplength=200, justify="left").pack()
        Button(item_frame, text="Mirar", command=lambda titulo=elem[1]: print(f"Título seleccionado: {titulo}"), bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="flat", width=15, height=1).pack(pady=5)

    content_continuar.update_idletasks()
    canvas_continuar.configure(scrollregion=canvas_continuar.bbox("all"))

    # Sección "Novedades"
    Label(f,text="Novedades",bg="#FFFFFF",fg="#000000",font=("Arial", 12, "bold"),wraplength=400,justify="center",).grid(row=5, column=0, columnspan=2, pady=5)

    frame_novedades = Frame(f, bg="#FFFFFF", width=450, height=100)
    frame_novedades.grid(row=6, column=0, columnspan=2, pady=5)

    canvas_novedades = Canvas(frame_novedades, bg="#FFFFFF", width=450, height=150, highlightthickness=0)
    scrollbar_novedades = Scrollbar(frame_novedades, orient="horizontal", command=canvas_novedades.xview)
    content_novedades = Frame(canvas_novedades, bg="#FFFFFF")

    canvas_novedades.configure(xscrollcommand=scrollbar_novedades.set)
    canvas_novedades.pack(side="top", fill="both", expand=True)
    scrollbar_novedades.pack(side="bottom", fill="x")

    canvas_novedades.create_window((0, 0), window=content_novedades, anchor="nw")

    for elem in listaNovedades:
        item_frame = Frame(content_novedades, bg="#FFFFFF")
        item_frame.pack(side="left", padx=10, pady=5)

        Label(item_frame, text=f"{elem[0]}", bg="#FFFFFF", fg="#000000", font=("Arial", 10), wraplength=200, justify="left").pack()
        Button(item_frame, text="Mirar", command=lambda titulo=elem[0]: print(f"Título seleccionado: {titulo}"), bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="flat", width=15, height=1).pack(pady=5)

    content_novedades.update_idletasks()
    canvas_novedades.configure(scrollregion=canvas_novedades.bbox("all"))

    f.pack(fill="both", expand=True)
    return f

def frame_multimedia(root, multimedia=[], equipo=[]):
    f=Frame(root)
    f.grid_propagate(False)
    #MULTIMEDIA
    titulo=multimedia[0]
    plot=multimedia[1]
    valoracion=multimedia[2]
    atp=multimedia[3]
    genero=multimedia[4]
    fecha_lanzamiento=multimedia[5]
    duracion=multimedia[6]
    
    Label(f, text=f"Titulo: {titulo}", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=10)
    Label(f, text=f"Plot: {plot}", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=10)
    Label(f, text=f"Valoracion: {valoracion}", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=10)
    Label(f, text=f"ATP: {atp}", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=10)
    Label(f, text=f"Genero: {genero}", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=10)
    Label(f, text=f"Fecha de lanzamiento: {fecha_lanzamiento}", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=10)
    Label(f, text=f"Duración: {duracion}", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=10)

    i=0
    for elem in equipo:
        for j in equipo[i]:
            Label(f, text=f"Nombre: {equipo[i][j]}", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=10)
            j+=1
        i+=1

    return f
