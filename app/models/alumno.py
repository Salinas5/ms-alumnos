from dataclasses import dataclass
from app import db

@dataclass
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    alumno_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    apellido: str = db.Column(db.String(100), nullable=False)
    nro_legajo: str = db.Column(db.String(20), unique=True, nullable=False)
    fechaIngreso: str = db.Column(db.String(10), nullable=False)
    fechaNacimiento: str = db.Column(db.String(10), nullable=False)
    tipoDocumento: str = db.Column(db.String(20), nullable=False)
    nroDocumento: str = db.Column(db.String(20), nullable=False, unique=True)
    sexo: str = db.Column(db.String(1), nullable=False)
    id_universidad = db.Column(db.Integer, db.ForeignKey('universidades.id'))

    universidad_rel = db.relationship("Universidad", back_populates="alumnos", foreign_keys=[id_universidad])
