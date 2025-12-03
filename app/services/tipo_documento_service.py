from app.models import TipoDocumento
from app.repositories.tipo_documento_repositorio import TipoDocumentoRepository
from app import cache

class TipoDocumentoService:
    @staticmethod
    def crear(tipo_documento: TipoDocumento) -> TipoDocumento:
        nuevo = TipoDocumentoRepository.crear(tipo_documento)
        cache.delete("tipos_documento_todos")
        cache.delete(f "tipo_documento_{nuevo.id}")
        return nuevo

    @staticmethod
    def buscar_por_id(id: int) -> TipoDocumento | None:
        cache_key = f"tipo_documento_{id}"
        tipo = cache.get(cache_key)
        if not tipo:
            tipo = TipoDocumentoRepository.buscar_por_id(id)
            if tipo:
                cache.set(cache_key, tipo, timeout=60)
        return tipo

    @staticmethod
    def buscar_todos() -> list[TipoDocumento]:
        tipos = cache.get("tipos_documento_todos")
        if not tipos:
            tipos = TipoDocumentoRepository.buscar_todos()
            cache.set("tipos_documento_todos", tipos, timeout=60)
        return tipos

    @staticmethod
    def actualizar(id: int, datos:dict) -> TipoDocumento | None:
        tipo = TipoDocumentoRepository.buscar_por_id(id)
        if not tipo:
            return None
        # Actualizamos campos directamente
        if 'nombre' in datos:
            tipo.nombre = datos['nombre']
        if 'sigla' in datos:
            tipo.sigla = datos['sigla']
        resultado = TipoDocumentoRepository.actualizar(tipo)
        if resultado:
            cache.delete(f"tipo_documento_{id}")
            cache.delete("tipos_documento_todos")
        return resultado

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        resultado = TipoDocumentoRepository.borrar_por_id(id)
        if resultado:
            cache.delete(f"tipo_documento_{id}")
            cache.delete("tipos_documento_todos")
        return resultado