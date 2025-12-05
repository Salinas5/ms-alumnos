import logging
from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    TESTING = False
    DEBUG = False
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PORT = os.getenv('REDIS_PORT', '6379')
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get( "DATABASE_URL", 
        "sqlite:///test.db")
    
class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"postgresql://{os.getenv('USER_DB','postgres')}:"
        f"{os.getenv('PASSWORD_DB','1234')}@"
        f"{os.getenv('HOST_DB','localhost')}:5432/"
        f"{os.getenv('NAME_DB','gestion_alumnos')}"
    )

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

def factory(app: str) -> Config:
    configuration = {
        'testing': TestConfig,
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    
    return configuration[app]