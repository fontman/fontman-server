""" Authentication controller

Handling authentication sessions between Fontman server and FMS client.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from flask import Blueprint, jsonify, request

from service import UserService

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/auth/login', methods=['POST'])
def login():
    auth_data = request.json
    user = UserService().find_by_username(auth_data["username"])

    try:
        if user.one() is not None:
            if user.username in auth_data["username"] and user.password in \
                    auth_data["password"]:
                return jsonify(user.uuid)

            else:
                return jsonify("unauthorized")

    except:
        return jsonify("unauthorized")


@auth_blueprint.route('/auth/add/user', methods=['POST'])
def add_new_user():
    user_data = request.json

    UserService().add_new(
        user_data["email"],
        user_data["name"],
        user_data["password"],
        user_data["username"]
    )
    confirm_data = UserService().find_by_username(user_data["username"]).first()

    response_data = {
        "user_id": confirm_data.user_id,
        "email": confirm_data.email,
        "name": confirm_data.name,
        "password": confirm_data.password,
        "username": confirm_data.username,
        "uuid": confirm_data.uuid
    }

    return jsonify(response_data)
