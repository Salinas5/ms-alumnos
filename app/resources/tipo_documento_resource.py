from flask import jsonify, Blueprint, request
from app.mapping.tipo_documento_schema import TipoDocumentoSchema
from app.services.tipo_documento_service import TipoDocumentoService


tipo_documento_bp = Blueprint('tipo_documento', __name__)
tipo_documentos_schema = TipoDocumentoSchema(many=True)
tipo_documento_schema = TipoDocumentoSchema()


@tipo_documento_bp.route('/', methods=['POST'])
def crear():
    data = request.get_json()
    tipo_documento = TipoDocumentoService.crear(**data)
    return jsonify(tipo_documento_schema.dump(tipo_documento)), 201

@tipo_documento_bp.route('/<int:tipo_documento_id>', methods=['GET'])
def buscar_por_id(tipo_documento_id):
    tipo = TipoDocumentoService.buscar_por_id(tipo_documento_id)
    if tipo:
        return jsonify(tipo_documento_schema.dump(tipo))
    return jsonify({'message': 'Tipo de documento not found'}), 404

@tipo_documento_bp.route('/', methods=['GET'])
def buscar_todos():
    tipos = TipoDocumentoService.buscar_todos()
    return jsonify(tipo_documentos_schema.dump(tipos))

@tipo_documento_bp.route('/<int:tipo_documento_id>', methods=['PUT'])
def actualizar(tipo_documento_id):
    data = request.get_json()
    actualizado = TipoDocumentoService.actualizar(tipo_documento_id, **data)
    if actualizado:
        return jsonify(tipo_documento_schema.dump(actualizado))
    return jsonify({'message': 'Tipo de documento not found'}), 404

@tipo_documento_bp.route('/<int:tipo_documento_id>', methods=['DELETE'])
def borrar_por_id(tipo_documento_id):
    borrado = TipoDocumentoService.borrar_por_id(tipo_documento_id)
    if borrado:
        return jsonify({'message': 'Tipo de documento deleted successfully'})
    return jsonify({'message': 'Tipo de documento not found'}), 404
