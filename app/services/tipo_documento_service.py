from app.models import TipoDocumento
from app.repositories.tipo_documento_repositorio import TipoDocumentoRepository

class TipoDocumentoService:
    @staticmethod
    def crear(tipo_documento: TipoDocumento) -> TipoDocumento | None:
        try:
            return TipoDocumentoRepository.crear(tipo_documento)
        except Exception:
            return None

    @staticmethod
    def buscar_por_id(id: int) -> TipoDocumento | None:
        try:
            return TipoDocumentoRepository.buscar_por_id(id)
        except Exception:
            return None

    @staticmethod
    def buscar_todos() -> list[TipoDocumento]:
        try:
            return TipoDocumentoRepository.buscar_todos()
        except Exception:
            return []

    @staticmethod
    def actualizar(id: int, datos:dict) -> TipoDocumento | None:
        try:
            tipo = TipoDocumentoRepository.buscar_por_id(id)
            if not tipo:
                return None
            
            if 'nombre' in datos:
                tipo.nombre = datos['nombre']
            if 'sigla' in datos:
                tipo.sigla = datos['sigla']
            
            return TipoDocumentoRepository.actualizar(tipo)
        except Exception:
            return None

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        try:
            return TipoDocumentoRepository.borrar_por_id(id)
        except Exception:
            return False