from dataclasses import dataclass
from app import db
from app.models.tipo_documento import TipoDocumento
from datetime import date

@dataclass
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    alumno_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nro_legajo: str = db.Column(db.String(20), unique=True, nullable=False)
    
    nombre: str = db.Column(db.String(100), nullable=False)
    apellido: str = db.Column(db.String(100), nullable=False)
    

    fechaIngreso: date = db.Column(db.Date, nullable=False)
    fechaNacimiento: date = db.Column(db.Date, nullable=False)

    tipo_documento_id: int = db.Column(db.Integer, db.ForeignKey('tipo_documento.id'), nullable=False)
    tipo_documento = db.relationship('TipoDocumento')

    nroDocumento: str = db.Column(db.String(20), nullable=False, unique=True)
    sexo: str = db.Column(db.String(1), nullable=False)
    id_universidad: int = db.Column(db.Integer, nullable=True)

    especialidad_id:int = db.Column(db.Integer, nullable=False)
