from app.repositories import AlumnoRepository
from app import db, cache
from app.models import Alumno

"""
Debemos agregar buscar alumno por legajo y dni, tambien agregar para
obtener certificados de alumno, y actualizar alumno.
"""

class AlumnoService:
    
    @staticmethod
    def crear_alumno(alumno):
        nuevo_alumno = AlumnoRepository.crear_alumno(alumno)
        # Limpiar cache relacionado
        cache.delete("alumnos_todos")
        cache.delete(f"alumno_{nuevo_alumno.id}")
        return nuevo_alumno
    
    @staticmethod
    def buscar_todos()-> list[Alumno]:
        alumnos = cache.get("alumnos_todos")
        if alumnos is None:
            alumnos = AlumnoRepository.buscar_todos()
            cache.set("alumnos_todos", alumnos, timeout=60)
        return alumnos
    
    @staticmethod
    def actualizar_alumno(alumno_id, alumno) -> Alumno | None:
        actualizado = AlumnoRepository.actualizar_alumno(alumno_id, alumno)
        if actualizado:
            cache.delete(f"alumno_{alumno_id}")
            cache.delete("alumnos_todos")
        return actualizado

    @staticmethod
    def buscar_por_id(alumno_id) -> Alumno | None:
        cache_key = f"alumno_{alumno_id}"
        alumno = cache.get(cache_key)
        if alumno is None:
            alumno = AlumnoRepository.buscar_alumno_id(alumno_id)
            cache.set(cache_key, alumno, timeout=60)
        return alumno

    @staticmethod
    def borrar_por_id(alumno_id) -> bool:
        resultado = AlumnoRepository.borrar_alumno_id(alumno_id)
        cache.delete(f"alumno_{alumno_id}")
        cache.delete("alumnos_todos")
        return resultado
