from app import db
from app.models.tipo_documento import TipoDocumento

class TipoDocumentoRepository:

    @staticmethod
    def crear(tipo_documento: TipoDocumento) -> TipoDocumento:
        db.session.add(tipo_documento)
        db.session.commit()
        return tipo_documento

    @staticmethod
    def buscar_por_id(id: int) -> TipoDocumento | None:
        return TipoDocumento.query.get(id)

    @staticmethod
    def buscar_todos() -> list[TipoDocumento]:
        return TipoDocumento.query.all()

    @staticmethod
    def actualizar(tipo_documento: TipoDocumento) -> TipoDocumento | None:
        tipo_documento_existente = db.session.merge(tipo_documento)
        db.session.commit()
        return tipo_documento_existente

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        tipo_documento = TipoDocumento.query.get(id)
        if not tipo_documento:
            return False
        db.session.delete(tipo_documento)
        db.session.commit()
        return True