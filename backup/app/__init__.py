from flask import Flask
from flask_restx import Api
from app.models.models import User, Cat
from flask_jwt_extended import JWTManager

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config=None)
    from app.exts import db, migrate
    db.init_app(app)
    migrate.init_app(db, app)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    JWTManager(app)
    api = Api(app, doc='/docs')
    api.add_namespace(name_auth)
    api.add_namespace(cat_ns)

    @app.shell_context_processor
    def create_context():
        return {
            "db": db,
            "Cat": Cat,  
            "user": User
            }
    return app


