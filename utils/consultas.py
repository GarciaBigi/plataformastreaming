from datetime import *
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
    select nombre,id_perfil 
    from perfiles p, usuarios u 
    where u.id_usuario = p.id_usuario and u.id_usuario = %s;
    """
    cursor.execute(consultaPerfiles,(idUsuario,))
    filaPer = cursor.fetchall()
    return filaPer

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
    select p.nombre , m2.titulo, m.porcentaje_visto 
    from perfiles p , miro m , multimedias m2 
    where p.id_perfil = m.id_perfil and m.id_multimedia = m2.id_multimedia and p.id_perfil = %s and m.porcentaje_visto < 100
    limit 5
    """
    cursor.execute(consultaContinuar,(idperfil,))
    filaContinuar = cursor.fetchall()
    return filaContinuar
def novedades(cursor):
    consultaNovedades = """
    select m.titulo 
    from multimedias m 
    order by m.fecha_agregacion desc
    limit 5
    """
    cursor.execute(consultaNovedades)
    listaNovedades = cursor.fetchall()
    return listaNovedades
