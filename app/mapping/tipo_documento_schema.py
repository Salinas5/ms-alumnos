from marshmallow import fields, Schema, post_load, validate
from app.models.tipo_documento import TipoDocumento

class TipoDocumentoSchema(Schema):
    id = fields.Int(dump_only=True)
    sigla = fields.String(required=True, validate=validate.Length(max=10))
    nombre = fields.String(required=True, validate=validate.Length(max=100))

    @post_load
    def make_tipo_documento(self, data, **kwargs):
        return TipoDocumento(**data)