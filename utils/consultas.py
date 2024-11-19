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