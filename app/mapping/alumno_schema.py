from marshmallow import Schema, fields, post_load, validate
from app.models.alumno import Alumno
from app.mapping.tipo_documento_schema import TipoDocumentoSchema

class AlumnoSchema(Schema):
    alumno_id = fields.Int(dump_only=True) 
    nro_legajo = fields.String(required=True, validate=validate.Length(max=20), data_key='numero_legajo')
    nombre = fields.String(required=True, validate=validate.Length(max=100))
    apellido = fields.String(required=True, validate=validate.Length(max=100))
    nroDocumento = fields.String(required=True, validate=validate.Length(max=20), data_key='numero_documento')
    tipo_documento_id = fields.String(required=True)
    tipo_documento = fields.Nested(TipoDocumentoSchema, dump_only=True)
    fechaNacimiento = fields.Date(required=True, data_key='fecha_nacimiento')
    sexo = fields.String(required=True, validate=validate.Length(max=1))
    fechaIngreso = fields.Date(required=True, data_key='fecha_ingreso')
    id_universidad = fields.Int(required=False)
    especialidad_id = fields.Int(required=False)
    
    @post_load
    def make_alumno(self, data, **kwargs):
        if 'especialidad_id' not in data:
            data['especialidad_id'] = 1 
            
        return Alumno(**data)