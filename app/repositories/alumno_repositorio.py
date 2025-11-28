from app import db
from app.models import Alumno

class AlumnoRepository:
    @staticmethod
    def crear_alumno(alumno) -> Alumno:
        """Crea un nuevo alumno en la base de datos"""
        db.session.add(alumno)
        db.session.commit()
        return alumno
    
    @staticmethod
    def buscar_todos() -> list[Alumno]:
        """Obtiene todos los alumnos"""
        return Alumno.query.all()
    
    @staticmethod
    def buscar_por_id(alumno_id) -> Alumno | None:
        """Obtiene un alumno por su ID"""
        return Alumno.query.get(alumno_id)
    
    @staticmethod
    def actualizar_alumno(alumno_id, alumno) -> Alumno | None:
        """Actualiza un alumno existente"""
        existing_alumno = AlumnoRepository.buscar_por_id(alumno_id)
        if existing_alumno:
            existing_alumno.nombre = alumno.nombre
            existing_alumno.apellido = alumno.apellido
            existing_alumno.email = alumno.email
            db.session.commit()
            return existing_alumno
        return None
    
    @staticmethod
    def borrar_por_id(alumno_id) -> bool:
        """Elimina un alumno por su ID"""
        alumno = AlumnoRepository.buscar_por_id(alumno_id)
        if alumno:
            db.session.delete(alumno)
            db.session.commit()
            return True
        return False