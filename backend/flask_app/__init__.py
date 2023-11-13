from flask import Flask
from flask_app.models import Cat, User
from flask_app.exts import db, migrate
from flask_restx import Api
from flask_cors import CORS, cross_origin

from flask_jwt_extended import JWTManager

def create_app(config):
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object(config)

    # Initialize flask extensions here
    
    db.init_app(app)
    migrate.init_app(app, db)
    app.config['SECRET_KEY'] = '\xcf3\xd3\xa9\x0f\xd1\xc9\xb7\xe2\xb3Q\x8f'
    JWTManager(app)
    api = Api(app, doc='/docs')
    
    # Register blueprints here
    from flask_app.cats import ns as cats_ns
    api.add_namespace(cats_ns)
    from flask_app.users import ns as users_ns
    api.add_namespace(users_ns)
    @app.shell_context_processor
    def create_context():
        return {
            "db": db,
            "Cat": Cat,
            "User": User 
        }
        
    return app
