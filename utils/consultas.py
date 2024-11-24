from datetime import *
#Todas las consultas SQL utilizadas
def con_usuarios(cursor, correo):
    consultaUsuario = f"""
    select *
    from usuarios
    where mail="{correo}";
    """
    cursor.execute(consultaUsuario)
    filaUsuario = cursor.fetchall()
    return filaUsuario
def ins_intento(cursor, estado, id):
    d=datetime.now()
    fecha=d.strftime("%Y-%m-%d")
    hora=d.strftime("%H:%M:%S")
    datos= (fecha,hora,estado,id)
    insertarIntento= """
    Insert into intentos(fecha,hora,exitosa, id_usuario)
    Values(%s, %s, %s, %s);
    """
    cursor.execute(insertarIntento,datos)

def con_perfiles(cursor, idUsuario):
    consultaPerfiles = """
    select nombre,id_perfil,p.tipo, u.id_usuario 
    from perfiles p, usuarios u 
    where u.id_usuario = p.id_usuario and u.id_usuario = %s;
    """
    cursor.execute(consultaPerfiles,(idUsuario,))
    filaPer = cursor.fetchall()
    return filaPer

def insert_perfil(cursor, nombre, tipo, id):
    insertarPerfil = """
    Insert into perfiles(nombre, tipo, id_usuario)
    Values(%s,%s,%s);
    """
    cursor.execute(insertarPerfil, (nombre, tipo, id))

def insert_usuario(cursor,correo,contrasena):
    insertarUsuario= """
    Insert into usuarios(mail,contrasena)
    Values(%s,%s)
    """
    cursor.execute(insertarUsuario,(correo,contrasena))
def upd_contrasena(cursor,correo,contrasena):
    print(correo)
    get_id= """
    select u.id_usuario 
    from usuarios u 
    where u.mail = %s;
    """
    cursor.execute(get_id,(correo,))
    id= cursor.fetchall()[0][0]

    upd_c="""
    UPDATE usuarios 
    SET contrasena = %s
    WHERE id_usuario = %s;
    """
    cursor.execute(upd_c,(contrasena,id))

def continuar_viendo(cursor,idperfil):
    consultaContinuar = """
    select p.nombre , m2.titulo, m.porcentaje_visto, m2.id_multimedia 
    from perfiles p , miro m , multimedias m2 
    where p.id_perfil = m.id_perfil and m.id_multimedia = m2.id_multimedia and p.id_perfil = %s and m.porcentaje_visto < 100
    limit 5
    """
    cursor.execute(consultaContinuar,(idperfil,))
    filaContinuar = cursor.fetchall()
    return filaContinuar

def novedades(cursor):
    consultaNovedades = """
    select m.titulo, m.id_multimedia
    from multimedias m 
    order by m.fecha_agregacion desc
    limit 5
    """
    cursor.execute(consultaNovedades)
    listaNovedades = cursor.fetchall()
    return listaNovedades

def novedadesFil(cursor, atp):
    consultaNovedades= """
    select m.titulo, m.id_multimedia 
    from multimedias m, perfiles p 
    where m.atp = %s 
    order by m.fecha_agregacion desc
    limit 5
    """
    cursor.execute(consultaNovedades, (atp,))
    listaNovedadesFil = cursor.fetchall()
    return listaNovedadesFil

def buscarTitulo(cursor, string):
    consultaBuscar = """
    select id_multimedia, titulo
    from multimedias m 
    where titulo like %s
    """
    string_aux = f"%{string}%"
    cursor.execute(consultaBuscar, (string_aux,))
    listaBuscar = cursor.fetchall()
    return listaBuscar

def buscarTituloFil(cursor,string,atp):
    consultaBuscar = """
    select id_multimedia, titulo
    from multimedias m
    where titulo like %s and m.atp = %s
    """
    string_aux = f"%{string}%"
    cursor.execute(consultaBuscar,(string_aux,atp))
    listaBuscar = cursor.fetchall()
    return listaBuscar

def buscarInfo(cursor, id):
    consultaTitulo= """
    select m.titulo ,m.valoracion , a.nombre ,a.apellido, ep.rol , m.duracion , m.plot , m.genero 
    from multimedias m , artistas a , equipo_produccion ep
    where m.id_multimedia = ep.id_multimedia  and ep.id_artista = a.id_artista and m.id_multimedia = %s
    """
    cursor.execute(consultaTitulo,(id,))
    listaInfo = cursor.fetchall()
    return listaInfo

def buscarInfoTi(cursor, titulo):
    consultaInfo = """
    select m.titulo ,m.valoracion , a.nombre ,a.apellido, ep.rol , m.duracion , m.plot , m.genero 
    from multimedias m , artistas a , equipo_produccion ep
    where m.id_multimedia = ep.id_multimedia  and ep.id_artista = a.id_artista and m.titulo = "%s"
    """
    cursor.execute(consultaInfo, (titulo,))
    listaInfo = cursor.fetchall()
    return listaInfo

def con_idmultimedia(cursor,titulo):
    consultarid="""
    select m.id_multimedia 
    from multimedias m 
    where m.titulo = %s
    """
    cursor.execute(consultarid,(titulo,))
    id=cursor.fetchall()[0][0]
    return id

def con_multimediafull(cursor,id):
    consultafull="""
    select titulo ,plot ,valoracion , atp, genero ,fecha_lanzamiento ,duracion 
    from multimedias m 
    where m.id_multimedia = %s
    """
    cursor.execute(consultafull,(id,))
    multimedia=cursor.fetchall()[0]
    return multimedia

def con_equipo(cursor,id):
    consultaequipo="""
    select a.nombre ,a.apellido , ep.rol 
    from multimedias m natural join equipo_produccion ep natural join artistas a 
    where m.id_multimedia = %s
    """
    cursor.execute(consultaequipo,(id,))
    equipo=cursor.fetchall()
    return equipo

def upd_mirar(cursor, id_titulo, id_perfil, visto, calificacion):
    upd_mirar = """
    UPDATE miro
    SET porcentaje_visto = %s, valoracion = %s
    WHERE id_perfil = %s AND id_multimedia = %s;
    """
    cursor.execute(upd_mirar, (visto, float(calificacion), id_perfil, id_titulo))

def con_vistoycalif(cursor,id_perfil, id_multimedia):
    consultavaloracion="""
    select m.porcentaje_visto , m.valoracion 
    from miro m 
    where m.id_perfil = %s and m.id_multimedia = %s
    """
    cursor.execute(consultavaloracion,(id_perfil,id_multimedia))
    relacion=cursor.fetchall()
    return relacion