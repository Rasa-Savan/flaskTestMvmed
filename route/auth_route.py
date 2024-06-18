import datetime

from flask import Blueprint, request, jsonify, render_template

from config import Config
from model.error_handling import validation_error, duplicate_username_email, exception, bad_request
from model.success_handling import success
from model.user_models import User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from marshmallow import ValidationError

from schema.schema import UserSchema

auth_bp = Blueprint('auth', __name__)

user_schema = UserSchema()


@auth_bp.route('/register', methods=['POST'])
def register():
    """
        This route serves to register a new user with 'POST' method

        request_body: json object
        username: string <min=5>
        email: string
        password: string <min=5, max=20>

        :return: json object with user's data
    """
    try:
        # Load request data into json format
        data = request.get_json()
        user_data = user_schema.load(data)
        username = user_data['username']
        email = user_data['email']

        # check the existing username and email which are unique field
        if User.get_existing_username_email(username, email):
            return duplicate_username_email(username, email)

        # save new user if it's valid format and there is no exist in database
        user = User(username=user_data['username'], email=user_data['email'])
        user.set_password(user_data['password'])
        user.save()

        message = "User has been successfully registered",
        data = {"username": username, "email": email}
        return success(message, data)

    except ValidationError as err:
        return validation_error(error=err.messages)
    except Exception as e:
        return exception(str(e))


@auth_bp.route('/login', methods=['POST'])
def login():
    """
        This route serves to log in a user with 'POST' method

        request_body: json object
        username: string
        password: string

        :return: json object with token and user's data
    """
    try:
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).one_or_404("There is no user: {0}".format(data['username']))

        # check user's object and compare password before create a token with expired time in 60min
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id, expires_delta=Config.JWT_ACCESS_TOKEN_EXPIRES)

            message = "Logged in successfully",
            data = {
                "username": user.username,
                "email": user.email,
                "access_token": access_token,
                "expires_in": datetime.datetime.now() + datetime.timedelta(minutes=60)
            }
            return success(message, data)
        else:
            return bad_request()

    except Exception as e:
        return exception(str(e))
