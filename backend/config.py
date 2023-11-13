
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    DEBUG = True
    TESTING = False

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql://flask_app:password@localhost:5432/flask_db'
    SQLALCHEMY_DATABASE_ECHO = True
    

class TestConfig(Config):
    pass

class StagingConfig(Config):
    pass

class ProdConfig(Config):
    pass
