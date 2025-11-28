from flask import Blueprint, jsonify, request
from app.mapping.alumno_schema import AlumnoSchema
from app.models.alumno import Alumno
from app import db

alumno_bp = Blueprint('alumno', __name__)
alumno_schema = AlumnoSchema()
alumnos_schema = AlumnoSchema(many=True)

@alumno_bp.route('/alumnos', methods=['GET'])
def get_alumnos():
    alumnos = Alumno.query.all()
    return jsonify(alumnos_schema.dump(alumnos)), 200

@alumno_bp.route('/alumnos/<string:numero_legajo>', methods=['GET'])
def get_alumno(numero_legajo):
    alumno = Alumno.query.get(numero_legajo)
    if not alumno:
        return jsonify({'error': 'Alumno no encontrado'}), 404
    return jsonify(alumno_schema.dump(alumno)), 200
 
@alumno_bp.route('/alumnos', methods=['POST'])
def create_alumno():
    data = request.get_json()
    try:
        alumno = alumno_schema.load(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    db.session.add(alumno)
    db.session.commit()
    return jsonify(alumno_schema.dump(alumno)), 201

@alumno_bp.route('/alumnos/<string:numero_legajo>', methods=['DELETE'])
def delete_alumno(numero_legajo):
    alumno = Alumno.query.get(numero_legajo)
    if not alumno:
        return jsonify({'error': 'Alumno no encontrado'}), 404
    db.session.delete(alumno)
    db.session.commit()
    return jsonify({'message': 'Alumno eliminado correctamente'}), 200