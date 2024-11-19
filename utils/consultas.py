from datetime import *
def con_usuarios(cursor, correo):
    consultaUsuario = f"""
    select *
    from usuarios
    where mail="{correo}";
    """
    cursor.execute(consultaUsuario)
    filaUsuario = cursor.fetchall()
    print(consultaUsuario)
    print(repr(correo))
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

