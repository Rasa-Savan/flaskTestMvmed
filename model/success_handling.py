from flask import jsonify

from schema.schema import Status


def success(message=None, data=None):
    response = {
        "status": Status.SUCCESS.value,
        "message": message if message is not None else None,
        "data": data
    }
    return jsonify(response), 200
