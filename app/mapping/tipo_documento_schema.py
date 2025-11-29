from marshmallow import fields, Schema, post_load, validate
from app.models.tipo_documento import TipoDocumento

class TipoDocumentoSchema(Schema):
    id = fields.Integer(required=True)
    nombre = fields.String(required=True, validate=validate.Length(max=50))
    descripcion = fields.String(required=True, validate=validate.Length(max=255))

    @post_load
    def make_tipo_documento(self, data, **kwargs):
        return TipoDocumento(**data)