from dataclasses import dataclass
from app import db

@dataclass
class TipoDocumento(db.Model):
    __tablename__ = 'tipo_documento'
    id: int = db.Column(db.Integer, primary_key=True)
    sigla: str = db.Column(db.String(10), nullable=False)
    nombre: str = db.Column(db.String(100), nullable=False)