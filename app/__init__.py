import logging  
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from app.config.cache_config import cache_config
from app.config.config import factory
from flask_marshmallow import Marshmallow
from app.route import RouteApp
from flask_caching import Cache

db = SQLAlchemy()
ma = Marshmallow()
cache = Cache()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app_context = os.getenv('FLASK_CONTEXT')
    #https://flask.palletsprojects.com/en/stable/api/#flask.Flask
    app = Flask(__name__)
    f = factory(app_context if app_context else 'development')
    app.config.from_object(f)
    
    db.init_app(app)
    cache.init_app(app, config=cache_config)
    route = RouteApp()
    route.init_app(app)
    
    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
