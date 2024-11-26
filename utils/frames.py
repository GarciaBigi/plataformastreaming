import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#Esta util se encarga de hacer los frames especificos para cada momento del programa
#Para lo mismo a todos los frames se le ingresa el root desde donde seran creados y datos de acurdo a lo que debera mostrar ese frame
#Luego se utilizan herramientas esteticas de la libreria tkinter para tener una interfaz grafica más sensilla
#Labels: son carteles que muestran el mensaje que halla en el parametro text=
#Entry: cuadros donde se pueden ingresar datos, el metodo .get() obtiene los datos ingresados
#Button: boton con el cual se llama cierta funcion en su parametro command= estos son la base de la comunicación entre el main y esta util
#ya que es posible utilizar funciones lambda para invocar funciones que hallan sido pasadas como objetos en los parametros de la función
#Canvas: es un widget que permite dibujar y manejar gráficos y otros elementos visuales, como si fuera un area de dibujo
#Scrollbar: son barras deslizantes para mostrar varios elementos de un canvas o frame
#Todos estos elementos tienen el atributo .pack() o .grid() , los cuales los apilan uno sobre otros o los ponene en cierta posicion de una grilla respectivamente
#Es importante analizar que siempre se retorna el frame, esto ya que el main es el encargado de poner o no los frames, este archivo es unicamente para diseño de interfaz

####FRAME DONDE SE INGRESA USUARIO Y CONTRASEÑA###############################################################################
def frame_ingreso(root, autenticacion,*,creacion=None, cambiocontra=None, nuevacreacion=False, nuevacontrasena=(False,"")):
    root.geometry("450x450")
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
####FRAME DONDE SE INGRESA USUARIO Y CONTRASEÑA###############################################################################


####FRAME DONDE SE MUESTRA LOS PERFILES ASOCIADOS A ESE USUARIO###############################################################
def frame_perfiles(root, listaPer, servicio, *, crearPerfil=None):

    root.geometry("650x450")
    f = Frame(root, bg="#FFFFFF", width=450, height=450)
    f.grid_propagate(False)
    
    # Etiqueta inicial
    Label(f, text="Bienvenido, seleccione un perfil.", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=20)

    # Contenedor para los perfiles
    canvas = Canvas(f, bg="#FFFFFF", highlightthickness=0, width=430, height=300)
    scrollbar = Scrollbar(f, orient="vertical", command=canvas.yview)
    profiles_frame = Frame(canvas, bg="#FFFFFF")

    canvas.create_window(0, 0, anchor="nw", window=profiles_frame)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Colocamos el canvas
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Frame para el formulario (invisible inicialmente)
    form_frame = Frame(f, bg="#FFFFFF")
    form_frame.pack(pady=10, fill="x")
    form_frame.pack_forget()  # Ocultar al principio

    def nuevoPer(idUsuario):
        # Mostrar el formulario
        form_frame.pack(pady=10, fill="x")
        form_frame.lift()

        # Variables de entrada
        tipo = StringVar()
        nombre = StringVar()

        # Campos de entrada y botón "Crear"
        Label(form_frame, text="Nombre del perfil:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).pack(pady=5)
        Entry(form_frame, width=30, bg="#F7F7F7", bd=1, relief="solid", textvariable=nombre).pack(pady=5)

        Label(form_frame, text="Tipo de perfil:", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).pack(pady=5)
        ttk.Combobox(form_frame, values=["Infantil", "Adulto"], textvariable=tipo).pack(pady=5)
        tipoBool = {"Infantil": True, "Adulto": False}

        if len(listaPer) <= 6:
            Button(form_frame,text="Crear Perfil",command=lambda: crearYActualizar(nombre.get(), tipoBool[tipo.get()], idUsuario),bg="#4CAF50",fg="#FFFFFF",font=("Arial", 10),relief="flat",).pack(pady=10)

    def crearYActualizar(nombre, tipo, idUsuario):
        # Ejecutar la función de creación de perfil
        if crearPerfil:
            crearPerfil(nombre, tipo, idUsuario,servicio)

        # Volver a agregar perfiles
    for i, perfil in enumerate(listaPer):
        Label(profiles_frame, text=f"{perfil[0]}", bg="#FFFFFF", fg="#000000", font=("Arial", 10)).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        Button(profiles_frame,text="Ingresar",command=lambda p=perfil: servicio(p),bg="#4CAF50",fg="#FFFFFF",font=("Arial", 10),relief="flat",width=10,).grid(row=i, column=1, padx=10, pady=5)

       # Si hay menos de 7 perfiles, mostrar el botón "Nuevo Perfil"
    if len(listaPer) < 7:
        Button(profiles_frame,text="Nuevo Perfil",command=lambda id=listaPer[0][3]: nuevoPer(id),bg="#FFFFFF",fg="#000000",font=("Arial", 10),).grid(row=len(listaPer), column=0, columnspan=2, pady=10)
    # Actualizar el canvas
    profiles_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    return f
####FRAME DONDE SE MUESTRA LOS PERFILES ASOCIADOS A ESE USUARIO###############################################################


####FRAME PARA LA CREACIÓN DE UN NUEVO USUARIO################################################################################
def frame_nuevacuenta(root, verificar):
    root.geometry("450x450")
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
####FRAME PARA LA CREACIÓN DE UN NUEVO USUARIO################################################################################

####FRAME PARA CAMBIAR LA CONTRASEÑA DE UN USUARIO YA EXISTENTE###############################################################
def frame_nuevacontra(root, usuario, nuevacontra):
    root.geometry("450x450")
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
####FRAME PARA CAMBIAR LA CONTRASEÑA DE UN USUARIO YA EXISTENTE###############################################################


####FRAME QUE MUESTRA EL CONTINUAR VIENDO, NOVEDADES Y BARRA DE BUSQUEDA DE LOS PERFILES######################################
def frame_plataforma(root, listaContinuar, listaNovedades, TipoPer, *,busq = "", vermultimedia=None):
    root.geometry("450x650")
    f = Frame(root, bg="#FFFFFF", width=450, height=600)
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
            vermultimedia(valor)


    def obtener_resultados(texto, TipoPer):
        listaBus.delete(0,END)
        resultados = busq(texto, TipoPer)
        for elem in resultados:
            listaBus.insert(END, elem[1])
        listaBus.bind('<<ListboxSelect>>', callback)
        listaBus.config(height=min(len(resultados), 10))
        

    busqueda = Entry(f, width=40, bg="#F7F7F7", bd=1, relief="solid")
    busqueda.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    botonBuscar = Button(f, text= "Buscar", command= lambda: obtener_resultados(busqueda.get(), TipoPer), bg="#2A2D43", fg= "#000000" ,font=("Arial", 10),relief="flat", width=8)
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

    frame_continuar = Frame(f, bg="#FFFFFF", width=450, height=70)
    frame_continuar.grid(row=4, column=0, columnspan=2, pady=2)
    
    canvas_continuar = Canvas(frame_continuar, bg="#FFFFFF", width=450, height=120, highlightthickness=0)
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
        Button(item_frame, text="Mirar", command=lambda t=elem[1]: vermultimedia(t), bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="flat", width=15, height=1).pack(pady=5)

    content_continuar.update_idletasks()
    canvas_continuar.configure(scrollregion=canvas_continuar.bbox("all"))

    # Sección "Novedades"
    Label(f,text="Novedades",bg="#FFFFFF",fg="#000000",font=("Arial", 12, "bold"),wraplength=400,justify="center",).grid(row=5, column=0, columnspan=2, pady=5)

    frame_novedades = Frame(f, bg="#FFFFFF", width=450, height=70)
    frame_novedades.grid(row=6, column=0, columnspan=2, pady=2)

    canvas_novedades = Canvas(frame_novedades, bg="#FFFFFF", width=450, height=120, highlightthickness=0)
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
        Button(item_frame, text="Mirar", command=lambda t=elem[0]: vermultimedia(t) , bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="flat", width=15, height=1).pack(pady=5)

    content_novedades.update_idletasks()
    canvas_novedades.configure(scrollregion=canvas_novedades.bbox("all"))

    f.pack(fill="both", expand=True)
    return f
####FRAME QUE MUESTRA EL CONTINUAR VIENDO, NOVEDADES Y BARRA DE BUSQUEDA DE LOS PERFILES######################################

####FRAME QUE MUESTRA LOS DATOS ESPECIFICOS DE LA MULTIMEDIA SELECCIONADA Y SU EQUIPO DE PRODUCCIÓN###########################
def frame_multimedia(root, *, visto="" ,calificacion="" ,mirarmultimedia=None, multimedia=[], equipo=[]):
    root.geometry("450x700")
    f = Frame(root, bg="#FFFFFF", width=450, height=450)
    f.grid_propagate(False)

    # MULTIMEDIA
    titulo, plot, valoracion, atp, genero, fecha_lanzamiento, duracion = multimedia

    # Título principal
    Label(f, text="Información de Multimedia", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=10)

    # Información principal de la multimedia
    info_frame = Frame(f, bg="#F7F7F7", relief="solid", bd=1, padx=10, pady=10)
    info_frame.pack(fill="x", padx=10, pady=10)

    Label(info_frame, text=f"Título: {titulo}", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").pack(fill="x", pady=5)
    Label(info_frame, text=f"Plot: {plot}", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w", wraplength=400, justify="left").pack(fill="x", pady=5)
    Label(info_frame, text=f"Valoración: {valoracion}", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").pack(fill="x", pady=5)
    Label(info_frame, text=f"ATP: {'Sí' if atp else 'No'}", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").pack(fill="x", pady=5)
    Label(info_frame, text=f"Género: {genero}", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").pack(fill="x", pady=5)
    Label(info_frame, text=f"Fecha de lanzamiento: {fecha_lanzamiento}", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").pack(fill="x", pady=5)
    Label(info_frame, text=f"Duración: {duracion} minutos", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").pack(fill="x", pady=5)

    # EQUIPO DE PRODUCCIÓN
    Label(f, text="Equipo de Producción", bg="#FFFFFF", fg="#000000", font=("Arial", 12, "bold"), wraplength=400, justify="center").pack(pady=10)

    equipo_frame = Frame(f, bg="#FFFFFF", width=450, height=150)
    equipo_frame.pack(pady=5)

    canvas_equipo = Canvas(equipo_frame, bg="#FFFFFF", width=450, height=150, highlightthickness=0)
    scrollbar_equipo = Scrollbar(equipo_frame, orient="horizontal", command=canvas_equipo.xview)
    content_equipo = Frame(canvas_equipo, bg="#FFFFFF")

    canvas_equipo.configure(xscrollcommand=scrollbar_equipo.set)
    canvas_equipo.pack(side="top", fill="both", expand=True)
    scrollbar_equipo.pack(side="bottom", fill="x")

    canvas_equipo.create_window((0, 0), window=content_equipo, anchor="nw")

    # Agregar miembros del equipo al contenedor
    for miembro in equipo:
        miembro_frame = Frame(content_equipo, bg="#F7F7F7", relief="solid", bd=1, padx=10, pady=10)
        miembro_frame.pack(side="left", padx=10, pady=10)

        Label(miembro_frame, text=f"Nombre: {miembro[0]}", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").pack(fill="x", pady=2)
        Label(miembro_frame, text=f"Apellido: {miembro[1]}", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").pack(fill="x", pady=2)
        Label(miembro_frame, text=f"Rol: {miembro[2]}", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").pack(fill="x", pady=2)

    # Actualizar región desplazable
    content_equipo.update_idletasks()
    canvas_equipo.configure(scrollregion=canvas_equipo.bbox("all"))
    # VER
    ver_frame = Frame(f, bg="#FFFFFF")  # Sin tamaño fijo
    ver_frame.pack(pady=10)

    canvas_ver = Canvas(ver_frame, bg="#FFFFFF", highlightthickness=0)  # Sin tamaño fijo
    content_ver = Frame(canvas_ver, bg="#FFFFFF")

    # Configura el canvas
    canvas_ver.pack(fill="both", expand=True)
    canvas_ver.create_window((0, 0), window=content_ver, anchor="nw")

    Label(content_ver, text=f"Porcentaje para ver (ya vistos: {visto}):", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    vista = Entry(content_ver, width=10, bg="#F7F7F7", bd=1, relief="solid")
    vista.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    Label(content_ver, text=f"Calificación personal entre 1 y 5 (actual: {calificacion}):", bg="#F7F7F7", fg="#000000", font=("Arial", 10), anchor="w").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    calif = Entry(content_ver, width=10, bg="#F7F7F7", bd=1, relief="solid")
    calif.grid(row=1, column=1, padx=10, pady=5, sticky="w")
    
    if visto=="0":
        firstime=True
    else:
        firstime=False

    Button(content_ver, text="Ver", command=lambda: mirarmultimedia(titulo,vista.get(),calif.get(),firstime), bg="#4CAF50", fg="#FFFFFF", font=("Arial", 10, "bold"), relief="flat").grid(row=2, column=0, columnspan=2, pady=10)

    content_ver.update_idletasks()
    canvas_ver.configure(scrollregion=canvas_ver.bbox("all"))

    f.pack(fill="both", expand=True)
    return f
####FRAME QUE MUESTRA LOS DATOS ESPECIFICOS DE LA MULTIMEDIA SELECCIONADA Y SU EQUIPO DE PRODUCCIÓN###########################
