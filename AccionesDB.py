from ConexionDB import ConectarDB

def login(carnet, password):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM usuarios WHERE carnet = %s && password = %s"
    valores = (carnet, password)
    cursor.execute(sentencia, valores)
    result = cursor.fetchone()
    print(type(result))
    #print(len(result))

    if result is None:
        print('No hay resultados')
        return False
    else:
        print('Si hay resultados' + str(result))
        return True

def buscarUserPorDUI(DUI):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM usuarios WHERE DUI = %s"
    valores = (DUI, )
    cursor.execute(sentencia, valores)
    result = cursor.fetchone()
    print(type(result))
    #print(len(result))

    if result is None:
        print('Usuario no existe')
        return False
    else:
        print('Usuario existente' + str(result))
        return True

def crearNombreUsuario(nombre, dui):
    iniciales = ''.join([palabra[0] for palabra in nombre.strip().split()])
    ultimosNum = str(dui)[-5:]
    print(iniciales + ultimosNum)
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



