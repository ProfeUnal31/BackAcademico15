from flask import jsonify,request,Blueprint
from Controlador.ControladorInscripcion import ControladorInscripcion
miControladorInscripcion=ControladorInscripcion()

inscripcion=Blueprint('inscripcion', __name__)

@inscripcion.route("/inscripciones",methods=['GET'])
def getInscripciones():
    json=miControladorInscripcion.index()
    return jsonify(json)
@inscripcion.route("/inscripciones/<string:id>",methods=['GET'])
def getInscripcion(id):
    json=miControladorInscripcion.show(id)
    return jsonify(json)
@inscripcion.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.create(data,id_estudiante,id_materia)
    return jsonify(json)
@inscripcion.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['PUT'])
def modificarInscripcion(id_inscripcion,id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.update(id_inscripcion,data,id_estudiante,id_materia)
    return jsonify(json)
@inscripcion.route("/inscripciones/<string:id_inscripcion>",methods=['DELETE'])
def eliminarInscripcion(id_inscripcion):
    json=miControladorInscripcion.delete(id_inscripcion)
    return jsonify(json)
@inscripcion.route("/inscripciones/materia/<string:id_materia>",methods=['GET'])
def inscritosEnMateria(id_materia):
    json=miControladorInscripcion.listarInscritosEnMateria(id_materia)
    return jsonify(json)
@inscripcion.route("/inscripciones/notas_mayores",methods=['GET'])
def getNotasMayores():
    json=miControladorInscripcion.notasMasAltasPorCurso()
    return jsonify(json)
@inscripcion.route("/inscripciones/promedio_notas/materia/<string:id_materia>",methods=['GET'])
def getPromedioNotasEnMateria(id_materia):
    json=miControladorInscripcion.promedioNotasEnMateria(id_materia)
    return jsonify(json)