from flask import Flask, jsonify, request

import AccionesDB

app = Flask(__name__)

@app.route('/insertar', methods=['POST'])
def insertar():
    datos = request.get_json()
    #print(datos)
    nombre = datos['nombre']
    apellido = datos['apellido']
    edad = datos['edad']
    AccionesDB.insertar(nombre, apellido, edad)
    jsonRespuesta = {"EstadoComms":"Usuario Ingresado Correctamente"}
    return jsonify(jsonRespuesta)

@app.route('/buscarUsuario', methods=['POST'])
def buscarUsuario():
    datos = request.get_json()
    print(datos)
    if AccionesDB.buscarUsuarios(datos['usuario'], datos['password']):
        jsonRespuesta = {"EstadoComms": "UsuarioExiste"}
    else:
        jsonRespuesta = {"EstadoComms": "UsuarioNoExiste"}

    return jsonify(jsonRespuesta)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

