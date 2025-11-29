from flask import jsonify, Blueprint, request
from app.mapping.tipo_documento_schema import TipoDocumentoSchema
from app.services.tipo_documento_service import TipoDocumentoService


tipo_documento_bp = Blueprint('tipo_documento', __name__)
tipo_documento_schema = TipoDocumentoSchema()

@tipo_documento_bp.route('/tipo_documento', methods=['POST'])
def create_tipo_documento():
    data = request.get_json()
    tipo_documento = MateriaService.create_tipo_documento(**data)
    return jsonify(tipo_documento_schema.dump(tipo_documento)), 201

@tipo_documento_bp.route('/tipo_documento/<int:tipo_documento_id>', methods=['GET'])
def get_tipo_documento(tipo_documento_id):
    tipo_documento = MateriaService.get_tipo_documento(tipo_documento_id)
    if tipo_documento:
        return jsonify(MateriaMapping.to_dict(tipo_documento))
    return jsonify({'message': 'Tipo de documento not found'}), 404

@tipo_documento_bp.route('/tipo_documento/<int:tipo_documento_id>', methods=['PUT'])
def update_tipo_documento(tipo_documento_id):
    data = request.get_json()
    tipo_documento = MateriaService.update_tipo_documento(tipo_documento_id, **data)
    if tipo_documento:
        return jsonify(MateriaMapping.to_dict(tipo_documento))
    return jsonify({'message': 'Tipo de documento not found'}), 404

@tipo_documento_bp.route('/tipo_documento/<int:tipo_documento_id>', methods=['DELETE'])
def delete_tipo_documento(tipo_documento_id):
    tipo_documento = MateriaService.delete_tipo_documento(tipo_documento_id)
    if tipo_documento:
        return jsonify({'message': 'Tipo de documento deleted successfully'})
    return jsonify({'message': 'Tipo de documento not found'}), 404
