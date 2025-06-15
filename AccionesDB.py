from ConexionDB import ConectarDB

def buscarUsuarios(carnet, password):
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

def insertar(nombre, apellido, edad):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "INSERT INTO usuarios (nombre, apellido, edad) VALUES (%s, %s, %s)"
    valores = (nombre, apellido, edad)
    cursor.execute(sentencia, valores)
    cursor.close()
    conexion.commit()
    conexion.close()

