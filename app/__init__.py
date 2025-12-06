import logging  
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.config.config import factory
from flask_marshmallow import Marshmallow
from app.route import RouteApp

db = SQLAlchemy()
ma = Marshmallow()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT', 'development')
    #https://flask.palletsprojects.com/en/stable/api/#flask.Flask
    app = Flask(__name__)
    f = factory(app_context)
    app.config.from_object(f)
    
    db.init_app(app)
    ma.init_app(app)
    route = RouteApp()
    route.init_app(app)
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app, "db": db, "ma": ma}

    return app
