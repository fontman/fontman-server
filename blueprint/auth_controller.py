""" Authentication controller

Handling authentication and user management between Fontman server and FMS
client.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from flask import Blueprint, jsonify, request

from service import UserService

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/auth/login', methods=['POST'])
def login():
    request_data = request.json
    user = UserService().find_by_email(request_data["email"]).first()

    try:
        if user is not None:
            if user.password in request_data["password"]:
                return jsonify(user.token)

            else:
                return jsonify({"error": "Invalid email or password"})

    except:
        return jsonify({"error": "Invalid email or password"})


@auth_blueprint.route('/auth/new/user', methods=['POST'])
def add_new_user():
    request_data = request.json

    try:
        if UserService().find_by_email(request_data["email"]).one() is not None:
            return jsonify({"error": "Email already exists"})

    except:
        user = UserService().add_new(
            email=request_data["email"],
            name=request_data["name"],
            password=request_data["password"]
        )

        return jsonify(
            {
                "user_id": user.user_id,
                "email": user.email,
                "name": user.name,
                "password": user.password,
                "token": user.token
            }
        )


@auth_blueprint.route('/auth/new/password', methods=['POST'])
def reset_password():
    request_data = request.json

    try:
        user = UserService().find_by_email(request_data["email"]).one()

        if user.token in request_data["token"]:
            UserService().update_by_email(
                request_data["email"],
                {
                    "password": request_data["password"]
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


@auth_blueprint.route('/auth/update/token', methods=['POST'])
def update_user_token():
    request_data = request.json

    try:
        user = UserService().find_by_email(request_data["email"]).one()

        if user.token in request_data["token"]:
            UserService().update_by_email(request_data["email"], {})
            renewed_user = UserService().find_by_email(request_data["email"])

            return jsonify({"token": renewed_user.token})

    except:
        return jsonify({"error": "Invalid request"})


@auth_blueprint.route('/auth/update/user', methods=['POST'])
def update_user_data():
    request_data = request.json

    try:
        if request_data["token"] in UserService().find_by_email(
                request_data["email"]
        ).one()["token"]:
            update_data = {
                "email": request_data["new_email"],
                "name": request_data["name"],
            }
            UserService().update_by_email(request_data["email"], update_data)

            renewed_user = UserService().find_by_email(
                request_data["new_email"]
            ).one()
            response_data = {
                "email": renewed_user.email,
                "name": renewed_user.name,
                "token": renewed_user.token
            }

            return jsonify(response_data)

    except:
        return jsonify({"error": "Invalid request"})
