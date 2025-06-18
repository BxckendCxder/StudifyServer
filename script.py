from flask import Flask, jsonify, request
from mysql.connector.tls_ciphers import APPROVED_TLS_CIPHERSUITES

import AccionesDB

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    if AccionesDB.login(datos['usuario'], datos['password']):
        jsonRespuesta = {"EstadoComms": "UsuarioExiste"}
    else:
        jsonRespuesta = {"EstadoComms": "UsuarioNoExiste"}
    return jsonify(jsonRespuesta)

@app.route('/buscarUserPorDUI', methods=['POST'])
def registrarUsuario():
    datos = request.get_json()
    if AccionesDB.registrarUsuario(datos['DUI']):
        jsonRespuesta = {"EstadoComms": "UsuarioExiste"}
    else:
        usuarioGen = AccionesDB.crearNombreUsuario(datos['Nombre'], datos['DUI'])
        jsonRespuesta = {"EstadoComms": "UsuarioNoExiste",
                         "NombreUsuario": usuarioGen}
        AccionesDB.agregarUsuario(usuarioGen, datos['Password'], datos['Nombre'], datos['FechaDNacimiento'], datos['telefono'], datos['DUI'])
    return jsonify(jsonRespuesta)

@app.route('/RegistrarMateria', methods=['POST'])
def registroMaterias():
    datos = request.get_json()
    if(AccionesDB.login(datos['usuario'], datos['password'])):
        AccionesDB.registroMaterias(datos['NombreMat'], datos['NombreProf'], datos['Horario'])
        jsonRespuesta = {"EstadoComms": "Materia agregada correctamente"}
    else:
        jsonRespuesta = {"EstadoComms": "Error"}
    return jsonify(jsonRespuesta)

@app.route('/listarMaterias', methods=['POST'])
def listarMaterias():
    lista = AccionesDB.listarMaterias()
    if not len(lista) == 0:
        jsonRespuesta = {"EstadoComms": "OK",
                         "Lista": lista}
    else:
        jsonRespuesta = {"EstadoComms": "Error"}
    print(jsonRespuesta)
    return jsonify(jsonRespuesta)

@app.route('/AgregarActividad', methods=['POST'])
def agregarActividad():
    datos = request.get_json()
    materia, descripcion, fechaSinFormato, categoria = datos['Materia'], datos['Descripcion'], datos['Fecha'], datos['Categoria']
    fecha = AccionesDB.formatoFecha(fechaSinFormato)
    matId = AccionesDB.buscarMatxNombre(materia)
    AccionesDB.agregarActividad(matId, descripcion, fecha, categoria)
    jsonRespuesta = {"EstadoComms": "OK"}
    return jsonify(jsonRespuesta)

@app.route('/InfoMateria', methods=['POST'])
def infoMateria():
    datos = request.get_json()
    resultado = AccionesDB.infoMateria(datos['Nombre'])
    if resultado is not None:
        informacion = {"EstadoComms": "OK",
                       "IdMateria":resultado[0],
                       "Nombre" : resultado[1],
                       "Profesor" : resultado[2],
                       "Horario" : resultado[3]
                       }
    else:
        informacion = {"EstadoComms": "Error"}
    return jsonify(informacion)

@app.route('/EliminarMateria', methods=['POST'])
def eliminarMateria():
    datos = request.get_json()
    result = AccionesDB.infoMateria(datos['Nombre'])
    idMat = result[0]
    AccionesDB.eliminarActividad(idMat)
    AccionesDB.eliminarMateria(datos['Nombre'])
    materias = AccionesDB.listarMaterias()
    jsonRespuesta = {"EstadoComms": "OK",
                     "lista": materias}
    return jsonify(jsonRespuesta)

@app.route('/ListarActividades', methods=['POST'])
def infoActividad():
    datos = request.get_json()
    idMat = AccionesDB.infoMateria(datos['NombreMat'])
    idMat = idMat[0]
    actividades = AccionesDB.infoActividades(idMat)
    resultado = []
    for fila in actividades:
        resultado.append({
            "NombreMat": datos['NombreMat'],
            "Categoria": fila[1],
            "Descripcion": fila[2],
            "FechaEntrega": fila[3].strftime('%d-%m-%Y'),
        })
    return jsonify({"actividades": resultado})

@app.route('/EliminarActividad', methods=['POST'])
def eliminarActividad():
    datos = request.get_json()
    Categoria = datos['Categoria']
    Descripcion = datos['Descripcion']
    idMat = AccionesDB.infoMateria(datos['NombreMat'])
    idMat = idMat[0]
    print(idMat, Categoria, Descripcion)
    AccionesDB.eliminarActividadInd(idMat, Categoria, Descripcion)
    informacion = {"EstadoComms": "OK"}
    return jsonify(informacion)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

