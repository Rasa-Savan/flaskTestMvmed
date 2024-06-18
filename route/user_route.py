from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from model.success_handling import success
from model.user_models import User
from schema.schema import UserResponseSchema

user_bp = Blueprint('user', __name__)


@user_bp.route('/all', methods=['GET'])
@jwt_required()
def get_all_users():
    """
    This route serves to list all user after logged in

    URL (Option):
    page=<number>&per_page=<number>

    Headers:
    Authorization: Bearer <token>

    :return: json object
    """
    try:
        current_user = get_jwt_identity()

        # users = User.query.all() # request all records

        page = request.args.get("page", default=1, type=int)
        per_page = request.args.get("per_page", default=5, type=int)
        users = User.query.paginate(page=page, per_page=per_page)

        data = {"user_data": UserResponseSchema(many=True).dump(users), "total": users.total}
        return success(data=data)

    except Exception as e:
        return jsonify({"msg": str(e)}), 500
