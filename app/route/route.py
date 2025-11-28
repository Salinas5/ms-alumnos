from flask import Flask

class RouteApp:
    def init_app(self, app: Flask) -> None:
        from app.resources import (alumno_bp)
        app.register_blueprint(alumno_bp, url_prefix='/api/alumnos')

