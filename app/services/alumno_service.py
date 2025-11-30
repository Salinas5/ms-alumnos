from app.repositories import AlumnoRepository
from app import db, cache
from app.models import Alumno


class AlumnoService:
    
    @staticmethod
    def crear_alumno(alumno: Alumno) -> Alumno:
        nuevo_alumno = AlumnoRepository.crear_alumno(alumno)
        # Limpiar cache relacionado
        cache.delete("alumnos_todos")
        cache.delete(f"alumno_{nuevo_alumno.alumno_id}")
        return nuevo_alumno
    
    @staticmethod
    def buscar_todos()-> list[Alumno]:
        alumnos = cache.get("alumnos_todos")
        if alumnos is None:
            alumnos = AlumnoRepository.buscar_todos()
            cache.set("alumnos_todos", alumnos, timeout=60)
        return alumnos
    
    @staticmethod
    def actualizar_alumno(alumno: Alumno) -> Alumno | None:
        actualizado = AlumnoRepository.actualizar_alumno(alumno)
        if actualizado:
            cache.delete(f"alumno_{alumno.alumno_id}")
            cache.delete("alumnos_todos")
        return actualizado

    @staticmethod
    def buscar_alumno_id(alumno_id: int) -> Alumno | None:
        cache_key = f"alumno_{alumno_id}"
        alumno = cache.get(cache_key)
        if alumno is None:
            alumno = AlumnoRepository.buscar_alumno_id(alumno_id)
            cache.set(cache_key, alumno, timeout=60)
        return alumno

    @staticmethod
    def borrar_alumno_id(alumno_id: int) -> bool:
        resultado = AlumnoRepository.borrar_alumno_id(alumno_id)
        cache.delete(f"alumno_{alumno_id}")
        cache.delete("alumnos_todos")
        return resultado
