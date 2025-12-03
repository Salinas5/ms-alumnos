from flask import jsonify, Blueprint, request
from app.mapping.tipo_documento_schema import TipoDocumentoSchema
from app.services.tipo_documento_service import TipoDocumentoService


tipo_documento_bp = Blueprint('tipo_documento', __name__)
tipo_documentos_schema = TipoDocumentoSchema(many=True)
tipo_documento_schema = TipoDocumentoSchema()


@tipo_documento_bp.route('/', methods=['POST'])
def crear():
    data = request.get_json()
    try:
        # Convertimos JSON a objeto
        nuevo_tipo = tipo_documento_schema.load(data)
        # Lo pasamos al servicio
        resultado = TipoDocumentoService.crear(nuevo_tipo)
        return jsonify(tipo_documento_schema.dump(resultado)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@tipo_documento_bp.route('/<int:id>', methods=['GET'])
def buscar_por_id(id):
    tipo = TipoDocumentoService.buscar_por_id(id)
    if tipo:
        return jsonify(tipo_documento_schema.dump(tipo)), 200
    return jsonify({'message': 'Tipo de documento no encontrado'}), 404

@tipo_documento_bp.route('/', methods=['GET'])
def buscar_todos():
    tipos = TipoDocumentoService.buscar_todos()
    return jsonify(tipo_documentos_schema.dump(tipos)), 200

@tipo_documento_bp.route('/<int:id>', methods=['PUT'])
def actualizar(id):
    data = request.get_json()
    try:
        actualizado = TipoDocumentoService.actualizar(id, data)
        if actualizado:
            return jsonify(tipo_documento_schema.dump(actualizado)), 200
        return jsonify({'message': 'Tipo de documento no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@tipo_documento_bp.route('/<int:tipo_documento_id>', methods=['DELETE'])
def borrar_por_id(id):
    borrado = TipoDocumentoService.borrar_por_id(id)
    if borrado:
        return jsonify({'message': 'Tipo de documento eliminado exitosamente'}), 200
    return jsonify({'message': 'Tipo de documento no encontrado'}), 404
