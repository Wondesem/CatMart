from flask import Flask, Blueprint

bp = Blueprint('main', __name__)
from app.main import auth, cat
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config=None)
    from app.exts import db, migrate
    db.init_app(app)
    migrate.init_app(db, app)  
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app