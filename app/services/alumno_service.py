from app.repositories import AlumnoRepository
# from app import cache # ELIMINAR
from app.models import Alumno


class AlumnoService:
    
    @staticmethod
    def crear_alumno(alumno: Alumno) -> Alumno:
        nuevo_alumno = AlumnoRepository.crear_alumno(alumno)
        return nuevo_alumno
    
    @staticmethod
    def buscar_todos()-> list[Alumno]:
        try:
            alumnos = AlumnoRepository.buscar_todos()
            return alumnos
        except Exception:
            return []
    
    @staticmethod
    def actualizar_alumno(alumno: Alumno) -> Alumno | None:
        actualizado = AlumnoRepository.actualizar_alumno(alumno)
        return actualizado

    @staticmethod
    def buscar_alumno_id(alumno_id: int) -> Alumno | None:
        alumno = AlumnoRepository.buscar_alumno_id(alumno_id)
        return alumno

    @staticmethod
    def borrar_alumno_id(alumno_id: int) -> bool:
        resultado = AlumnoRepository.borrar_alumno_id(alumno_id)
        return resultado