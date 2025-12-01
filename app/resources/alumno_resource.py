from flask import Blueprint, jsonify, request
from app.mapping.alumno_schema import AlumnoSchema
from app.services.alumno_service import AlumnoService
from app.models.alumno import Alumno

alumno_bp = Blueprint('alumno_bp', _name_)
alumno_schema = AlumnoSchema()
alumnos_schema = AlumnoSchema(many=True)

# GET /api/alumnos
@alumno_bp.route('/', methods=['GET'])
def get_alumnos():
    alumnos = AlumnoService.buscar_todos()
    return jsonify(alumnos_schema.dump(alumnos)), 200

# GET /api/alumnos/<alumno_id>
@alumno_bp.route('/<int:alumno_id>', methods=['GET'])
def get_alumno(alumno_id):
    alumno = AlumnoService.buscar_alumno_id(alumno_id)
    if not alumno:
        return jsonify({'error': 'Alumno no encontrado'}), 404
    return jsonify(alumno_schema.dump(alumno)), 200

# POST /api/alumnos
@alumno_bp.route('/', methods=['POST'])
def create_alumno():
    data = request.get_json()
    try:
        alumno = alumno_schema.load(data)
        alumno = AlumnoService.crear_alumno(alumno)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify(alumno_schema.dump(alumno)), 201

# PUT /api/alumnos/<alumno_id>
@alumno_bp.route('/<int:alumno_id>', methods=['PUT'])
def update_alumno(alumno_id):
    data = request.get_json()
    alumno = AlumnoService.buscar_alumno_id(alumno_id)
    if not alumno:
        return jsonify({'error': 'Alumno no encontrado'}), 404
    try:
        for key, value in data.items():
            setattr(alumno, key, value)
        alumno = AlumnoService.actualizar_alumno(alumno)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    return jsonify(alumno_schema.dump(alumno)), 200

# DELETE /api/alumnos/<alumno_id>
@alumno_bp.route('/<int:alumno_id>', methods=['DELETE'])
def delete_alumno(alumno_id):
    resultado = AlumnoService.borrar_alumno_id(alumno_id)
    if not resultado:
        return jsonify({'error': 'Alumno no encontrado'}), 404
    return jsonify({'message': 'Alumno eliminado correctamente'}), 200