from dataclasses import dataclass
from app import db

@dataclass
class TipoDocumento(db.Model):
    __tablename__ = 'tipo_documento'
    dni: int = db.Column(db.Integer, primary_key=True)
    libreta_civica: int = db.Column(db.Integer, nullable=False)
    libreta_enrolamiento: int = db.Column(db.Integer, nullable=False)
    pasaporte: int = db.Column(db.Integer, nullable=False)