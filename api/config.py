"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    AWS_SECRET_KEY = environ.get('AWS_SECRET_KEY')
    AWS_KEY_ID = environ.get('AWS_KEY_ID')
    @staticmethod
    def get_config():
        _env = environ.get("FLASK_ENV")
        if not _env:
            raise ValueError("FLASK_ENV environemnt variable Required")
        _config = environ.get('APP_CFG')
        if not _config:
            raise ValueError("APP_CFG environemnt variable Required")
        return _config

class ProdConfig(Config):
    DEBUG = False
    TESTING = False
class DevConfig(Config):
    DEBUG = True
    TESTING = True