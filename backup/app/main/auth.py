from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.models.models import User
from werkzeug.security import  generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

from app.main import bp

# User sign up serialization

signup_model = bp.model(
    "SignUp",
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String()
    }
)

login_model = bp.model(
    "Login",
    {
        "username": fields.String(),
        "email": fields.String()
    }
)
@bp.route('/signup')
class SignUp(Resource):
    @bp.expect(signup_model)
    def post(self):
        data = request.get_json()

        username = data.get('username')
        db_user = User.query.filter_by(username=username).first()
        if db_user is not None:
            return jsonify(
                {"Message":
                 f"username '{username}' already exists. try another one."}
                 )
        new_user = User(username=data.get('username'),
                        email=data.get('email'),
                        password=generate_password_hash(data.get('password'))
                        )
        new_user.save()
        return jsonify(
            {"message": f"username '{username}' is created succefully"}
            )


@bp.route('/login')
class Login(Resource):
    @bp.expect(login_model)
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        db_user = User.query.filter_by(username=username).first()
        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.username)
            refresh_token = create_refresh_token(identity=db_user.username)
            return jsonify(
                {
                    "access token": access_token,
                    "refresh token": refresh_token
                }
            )
        else:
            return jsonify({"message": "Username or password is not correct"})