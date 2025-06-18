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

def listarMaterias():
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM studyfy.materias "
    cursor.execute(sentencia)
    result = cursor.fetchall()
    #print(len(result))
    lista = []
    for x in result:
        lista.append(x[1])
    return lista

def agregarActividad(materia, descripcion, fecha, categoria):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = ("INSERT INTO `studyfy`.`registroactividad` (`Categoria`,`Descripcion`,` FechaEntrega`,`Id_Materia`) "
                 "VALUES (%s, %s, %s, %s);")
    valores = (categoria, descripcion, fecha, materia)
    cursor.execute(sentencia, valores)
    cursor.close()
    conexion.commit()
    conexion.close()
    return True

def formatoFecha(fecha):
    # Diccionario de meses en inglés a números
    meses = {
        "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4,
        "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8,
        "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12
    }
    mes_str, dia_str, anio_str = fecha.strip().split()
    mes = meses[mes_str.upper()]
    dia = dia_str
    anio = anio_str
    fecha = str(anio) + "-" + str(mes) + "-" +str(dia)
    return fecha

def buscarMatxNombre(materia):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM studyfy.materias WHERE nombre = %s"
    valores = (materia,)
    cursor.execute(sentencia, valores)
    result = cursor.fetchone()
    return result[0]

def infoMateria(nombre):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM studyfy.materias WHERE nombre = %s"
    valores = (nombre,)
    cursor.execute(sentencia, valores)
    result = cursor.fetchone()
    return result

def eliminarMateria(nombre):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "DELETE FROM studyfy.materias WHERE nombre = %s;"
    valores = (nombre,)
    cursor.execute(sentencia, valores)
    cursor.close()
    conexion.commit()
    conexion.close()
    return True

def eliminarActividad(idMateria):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "DELETE FROM studyfy.registroactividad WHERE Id_Materia = %s;"
    valores = (idMateria,)
    cursor.execute(sentencia, valores)
    cursor.close()
    conexion.commit()
    conexion.close()
    return True

def infoActividades(idMat):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "SELECT * FROM studyfy.registroactividad WHERE Id_Materia = %s"
    valores = (idMat,)
    cursor.execute(sentencia, valores)
    result = cursor.fetchall()
    return result

def eliminarActividadInd(idMat, categoria, descripcion):
    conexion = ConectarDB()
    cursor = conexion.cursor()
    sentencia = "DELETE FROM studyfy.registroactividad WHERE Id_Materia = %s AND Categoria = %s AND Descripcion = %s;"
    valores = (idMat, categoria, descripcion)
    cursor.execute(sentencia, valores)
    cursor.close()
    conexion.commit()
    conexion.close()
    return True


