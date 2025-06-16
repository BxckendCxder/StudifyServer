from flask import Flask, jsonify, request

import AccionesDB

app = Flask(__name__)

@app.route('/insertar', methods=['POST'])
def insertar():
    datos = request.get_json()
    nombre = datos['nombre']
    apellido = datos['apellido']
    edad = datos['edad']
    AccionesDB.insertar(nombre, apellido, edad)
    jsonRespuesta = {"EstadoComms":"Usuario Ingresado Correctamente"}
    return jsonify(jsonRespuesta)

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
    print(datos)
    if(AccionesDB.login(datos['usuario'], datos['password'])):
        AccionesDB.registroMaterias(datos['NombreMat'], datos['NombreProf'], datos['Horario'])
        jsonRespuesta = {"EstadoComms": "Materia agregada correctamente"}
    else:
        jsonRespuesta = {"EstadoComms": "Error"}
    return jsonify(jsonRespuesta)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

