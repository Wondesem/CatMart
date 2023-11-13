from flask_restx import Namespace
ns = Namespace("cats", description="A namespace for cat routes")
from flask_app.cats import catroute