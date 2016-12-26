""" User controller

Register users, authenticate user sessions.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

from flask import Blueprint, jsonify, request

from service import UserService

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/user/add', methods=['POST'])
def add_new_user():
    user_data = request.json

    print(user_data)
    UserService().add_new(
        email=user_data["email"],
        name=user_data["name"],
        secret=user_data["secret"]
    )

    user = UserService().find_by_email(user_data["email"]).one()

    return jsonify(
        {
            "user_id": user.id,
            "email": user.email,
            "key": user.key,
            "name": user.name,
        }
    )


@user_blueprint.route('/user/all', methods=['GET'])
def find_all_users():
    users_list = []

    for user in UserService().find_all():
        users_list.append(
            {
                "id": user.id,
                "email": user.email,
                "name": user.name,
            }
        )

    return jsonify(users_list)


@user_blueprint.route('/user/validate', methods=['POST'])
def validate_user():
    validation_data = request.json
    secret = UserService().find_by_email(validation_data["email"]).one().secret

    return jsonify(validation_data["secret"] == secret)
