from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity
from flask_login import current_user
from flask_restx import Resource, fields
from werkzeug.security import generate_password_hash, check_password_hash
from flask_app.models import User 
from flask_app.users import ns


signup_model = ns.model(
    "SignUp",
    {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String()
    }
)

login_model = ns.model(
    "Login",
    {
        "username": fields.String(),
        "password": fields.String()
    }
)
@ns.route('/signup')
class SignUp(Resource):
    @ns.expect(signup_model)
    def post(self):
        data = request.get_json()
        username=data.get('username')
    
        db_user = User.query.filter_by(username=username).first()
        if db_user is not None:
            return jsonify({
                "message": f"User '{username}' already exists"
            })
        else:
            new_user = User(
            username=data.get('username'),
            email=data.get('email'),
            password=generate_password_hash(data.get('password'))
        )
            new_user.save()

            return jsonify({"message": f"The user '{username}' is successfully created."})
     

@ns.route('/login')
class Login(Resource):
    @ns.expect(login_model)
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        db_user = User.query.filter_by(username=username).first()

        if db_user and check_password_hash(db_user.password, password):
            access_token = create_access_token(identity=db_user.username)
            refresh_token = create_refresh_token(identity=db_user.username)

            return jsonify({"access_token ": access_token,
                            "refresh_token": refresh_token})
        else:
            return jsonify({"message": "Eihter the username or the password is invalid."})
    

    @ns.route('/refresh')
    class RefreshTokResoure(Resource):
        @jwt_required(True)
        def post(self):
            current_user = get_jwt_identity()
            new_access_token = create_access_token(identity=current_user)
            return make_response(jsonify({"access_token": new_access_token}), 200)