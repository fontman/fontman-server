""" Users controller

REST blueprint to do user management.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/1/2017
"""

from flask import Blueprint, jsonify, request

from service import UserService

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/users')
def find_all_users():
    response_data = []

    for user in UserService().find_all():
        response_data.append(
            {
                "user_id": user.user_id,
                "email": user.email,
                "name": user.name,
            }
        )

    return jsonify(response_data)


@users_blueprint.route('/users/<user_id>')
def find_user_by_user_id(user_id):
    try:
        user = UserService().find_by_user_id(user_id).one()

        return jsonify(
            {
                "user_id": user.user_id,
                "email": user.email,
                "name": user.name
            }
        )

    except:
        return jsonify({"error": "Invalid request"})
