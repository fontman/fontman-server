""" Authentication controller

Handling authentication and user management between Fontman server and FMS
client.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from service import UserService

from flask import Blueprint, jsonify, request
from passlib.hash import bcrypt

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/auth/login', methods=['POST'])
def login():
    request_data = request.json
    user = UserService().find_by_email(request_data["email"]).first()

    try:
        if user is not None:
            UserService().update_by_email(request_data["email"], {})
            user = UserService().find_by_email(request_data["email"]).first()

            if bcrypt.verify(request_data["password"], user.password):
                return jsonify(
                    {
                        "user_id": user.user_id,
                        "token": user.token
                    }
                )

            else:
                return jsonify({"error": "Invalid email or password"})

        else:
            return jsonify({"error": "Invalid email or password"})

    except:
        raise


@auth_blueprint.route('/auth/new/user', methods=['POST'])
def add_new_user():
    request_data = request.json

    if UserService().find_by_email(request_data["email"]).first() is not None:
            return jsonify({"error": "Email already exists"})

    else:
        user = UserService().add_new(
            email=request_data["email"],
            name=request_data["name"],
            password=bcrypt.encrypt(request_data["password"])
        )

        return jsonify(
            {
                "user_id": user.user_id,
                "email": user.email,
                "name": user.name,
                "token": user.token
            }
        )


@auth_blueprint.route('/auth/new/password', methods=['POST'])
def reset_password():
    request_data = request.json

    try:
        user = UserService().find_by_email(request_data["email"]).first()

        if bcrypt.verify(request_data["old_password"], user.password):
            UserService().update_by_email(
                request_data["email"],
                {
                    "password": bcrypt.encrypt(request_data["password"])
                }
            )
            renewed_user = UserService().find_by_email(request_data["email"])

            return jsonify(
                {
                    "password": renewed_user["password"],
                    "token": renewed_user["token"]
                }
            )

        else:
            return {"error": "Token error, contact administrator"}

    except:
        return jsonify({ "error": "Invalid username or password"})


@auth_blueprint.route('/auth/update/user', methods=['POST'])
def update_user_data():
    request_data = request.json

    try:
        if request_data["token"] in UserService().find_by_email(
                request_data["email"]
        ).first()["token"]:
            update_data = {
                "email": request_data["new_email"],
                "name": request_data["name"],
            }
            UserService().update_by_email(request_data["email"], update_data)

            renewed_user = UserService().find_by_email(
                request_data["new_email"]
            ).first()
            response_data = {
                "email": renewed_user.email,
                "name": renewed_user.name,
                "token": renewed_user.token
            }

            return jsonify(response_data)

    except:
        return jsonify({"error": "Invalid request"})
