from ConexionDB import ConectarDB

def login(carnet, password):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM usuarios WHERE carnet = %s && password = %s"
    valores = (carnet, password)
    cursor.execute(sentencia, valores)
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return True

def registrarUsuario(DUI):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM usuarios WHERE DUI = %s"
    valores = (DUI, )
    cursor.execute(sentencia, valores)
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        return True

def crearNombreUsuario(nombre, dui):
    iniciales = ''.join([palabra[0] for palabra in nombre.strip().split()])
    ultimosNum = str(dui)[-5:]
    return iniciales + ultimosNum

def agregarUsuario(carnet, password, nombre, fechaDNacimiento, telefono, DUI):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "INSERT INTO studyfy.usuarios (carnet, password, nombre, fechaDeNacimiento, Telefono, DUI) values (%s, %s, %s, %s, %s, %s)"
    valores = (carnet, password, nombre, fechaDNacimiento, telefono, DUI)
    cursor.execute(sentencia, valores)
    cursor.close()
    conexion.commit()
    conexion.close()
    return True

def registroMaterias(nombreMat, nombreProf, horario):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "INSERT INTO studyfy.materias (nombre, profesor, Horario) VALUES (%s, %s, %s)"
    valores = (nombreMat, nombreProf, horario)
    cursor.execute(sentencia, valores)
    cursor.close()
    conexion.commit()
    conexion.close()
    return True




