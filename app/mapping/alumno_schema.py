from marshmallow import Schema, fields, post_load, validate
from app.models.alumno import Alumno

class AlumnoSchema(Schema):
    numero_legajo = fields.String(required=True, validate=validate.Length(max=20))
    nombre = fields.String(required=True, validate=validate.Length(max=100))
    apellido = fields.String(required=True, validate=validate.Length(max=100))
    numero_documento = fields.String(required=True, validate=validate.Length(max=20))
    tipo_documento = fields.String(required=True, validate=validate.Length(max=20))
    fecha_nacimiento = fields.Date(required=True)
    sexo = fields.String(required=True, validate=validate.Length(max=10))
    fecha_ingreso = fields.Date(required=True)

    @post_load
    def make_alumno(self, data, **kwargs):
        return Alumno(**data)