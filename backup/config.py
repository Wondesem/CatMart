from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATION = \
        config('SQLALCHEMY_TRACK_MODIFICATION', cast=bool)
    DEBUG = False


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR, 'dev.db')
    SQLALCHEMY_DATABASE_ECHO = True
    DEBUG = True


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass
