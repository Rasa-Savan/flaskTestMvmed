from flask import jsonify, Blueprint

from extensions import jwt
from schema.schema import Status

error_bp = Blueprint('error_handling', __name__)


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    response = {
        "status": Status.ERROR.value,
        "type": "token_expired",
        "message": "token is expired"
    }
    return jsonify(response), 401


@jwt.invalid_token_loader
def invalid_token_callback(error_header):
    response = {
        "status": Status.ERROR.value,
        "type": "invalid_token",
        "message": error_header
    }
    return jsonify(response), 401


@jwt.unauthorized_loader
def missing_token_callback(error_header):
    response = {
        "status": Status.ERROR.value,
        "type": "missing_token",
        "message": error_header
    }
    return jsonify(response), 401


def validation_error(error):
    response = {
        "status": Status.ERROR.value,
        "type": "validation_error",
        "message": error
    }
    return jsonify(response), 400


def duplicate_username_email(username, email):
    response = {
        "status": Status.ERROR.value,
        "type": "duplicate_username_email",
        "message": "Username: {0} or email: {1} are already exists".format(username, email)
    }
    return jsonify(response), 400


def bad_request():
    response = {
        "status": Status.ERROR.value,
        "type": "bad_request",
        "message": "Username and password is incorrect, please try again"
    }
    return jsonify(response), 400


def exception(error):
    response = {
        "status": Status.ERROR.value,
        "type": "internal_server_error",
        "message": error
    }
    return jsonify(response), 500
