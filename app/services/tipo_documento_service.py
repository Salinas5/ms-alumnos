from app.models import TipoDocumento
from app.repositories.tipo_documento_repositorio import TipoDocumentoRepository
from app import db, cache
class TipoDocumentoService:
    @staticmethod
    def crear(tipo_documento) -> TipoDocumento:
        nuevo_tipo_documento = TipoDocumentoRepository.crear(tipo_documento)
        cache.delete("tipos_documento_todos")
        cache.delete(f"tipo_documento_{nuevo_tipo_documento.id}")
        return nuevo_tipo_documento

    @staticmethod
    def buscar_por_id(dni: int) -> TipoDocumento | None:
        cache_key = f"tipo_documento_{dni}"
        tipo_documento = cache.get(cache_key)
        if not tipo_documento:
            tipo_documento = TipoDocumentoRepository.buscar_por_id(dni)
            cache.set(cache_key, tipo_documento, timeout=60)
        return tipo_documento

    @staticmethod
    def buscar_todos() -> list[TipoDocumento]:
        cache_key = "tipos_documento_todos"
        tipos_documento = cache.get(cache_key)
        if not tipos_documento:
            tipos_documento = TipoDocumentoRepository.buscar_todos()
            cache.set(cache_key, tipos_documento, timeout=60)
        return tipos_documento

    @staticmethod
    def actualizar(tipo_documento) -> TipoDocumento | None:
        resultado = TipoDocumentoRepository.actualizar(tipo_documento)
        cache.delete(f"tipo_documento_{tipo_documento.id}")
        cache.delete("tipos_documento_todos")
        return resultado

    @staticmethod
    def borrar_por_id(dni: int) -> bool:
        resultado = TipoDocumentoRepository.borrar_por_id(dni)
        cache.delete(f"tipo_documento_{dni}")
        cache.delete("tipos_documento_todos")
        return resultado