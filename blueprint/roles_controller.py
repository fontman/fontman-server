""" Roles controller

REST blueprint to do user role management.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/1/2017
"""

from flask import Blueprint, jsonify, request

from service import RoleService
from service import UserService

roles_blueprint = Blueprint("roles_blueprint", __name__)


@roles_blueprint.route("/roles/<entity>/<entity_id>/")
def find_roles_by_entity_id(entity, entity_id):
    try:
        query_string = request.args.get("user_id")
        role = RoleService().find_role(entity, entity_id, query_string).one()

        return jsonify(
            {
                "role": role.role
            }
        )

    except:
        return jsonify({"error": "Unauthorized action"})


@roles_blueprint.route("/roles/new", methods=["POST"])
def add_new_role():
    request_data = request.json

    try:
        if request_data["token"] in UserService().find_by_user_id(
                request_data["user_id"]
        ).one().token:
            new_role = RoleService().add_new(
                request_data["entity"],
                request_data["entity_id"],
                request_data["role"],
                request_data["user_id"]
            )

            return jsonify(
                {
                    "role_id": new_role.role_id,
                    "entity": new_role.entity,
                    "entity_id": new_role.entity_id,
                    "role": new_role.role,
                    "user_id": new_role.user_id
                }
            )

        else:
            return jsonify({"error": "Unauthorized action"})

    except:
        return jsonify({"error": "Error while creating new role"})


@roles_blueprint.route("/roles/<role_id>/delete", methods=["POST"])
def delete_role_by_role_id(role_id):
    request_data = request.json

    try:
        RoleService().delete_by_role_id(role_id)
        return jsonify(True)

    except:
        return jsonify({"error": "Invalid request"})


@roles_blueprint.route("/roles/<role_id>/updade")
def update_role_by_role_id(role_id):
    request_data = request.json

    try:
        RoleService().update_by_role_id(
            role_id,
            {
                "role": request_data["new_role"]
            }
        )
        role = RoleService().find_by_role_id(role_id).one()

        return jsonify({"role": role.role})

    except:
        return jsonify({"error": "Invalid request"})
