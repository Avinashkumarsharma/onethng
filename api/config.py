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

class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False