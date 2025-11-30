from app import db
from app.models import Alumno

class AlumnoRepository:
    @staticmethod
    def crear_alumno(alumno) -> Alumno:
        db.session.add(alumno)
        db.session.commit()
        return alumno

    @staticmethod
    def buscar_todos() -> list[Alumno]:
        return Alumno.query.all()
    
    @staticmethod
    def buscar_alumno_id(alumno_id) -> Alumno | None:
        return Alumno.query.get(alumno_id)
    
    @staticmethod
    def actualizar_alumno(alumno) -> Alumno | None:
        db.session.merge(alumno)
        db.session.commit()
        return alumno
    
    @staticmethod
    def borrar_alumno_id(alumno_id: int) -> bool:
        alumno = db.session.query(Alumno).filter_by(alumno_id=alumno_id).first()
        if not alumno:
            return False
        db.session.delete(alumno)
        db.session.commit()
        return True