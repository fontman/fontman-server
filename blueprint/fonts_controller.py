""" Font collections controller

REST blueprint to manipulate font collections database.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/1/2017
"""

from flask import Blueprint, jsonify, request

from consumer import GitHubConsumer
from service import FontFaceService
from service import FontService
from service import RoleService
from service import UserService

fonts_blueprint = Blueprint('fonts_blueprint', __name__)


@fonts_blueprint.route('/fonts')
def find_all_fonts():
    response_data = []
    fonts = FontService().find_all()

    for font in fonts:
        response_data.append(
            {
                "font_id": font.font_id,
                "channel_id": font.channel_id,
                "name": font.name,
                "team_id": font.team_id,
                "type": font.type
            }
        )

    return jsonify(response_data)


@fonts_blueprint.route('/fonts/<font_id>')
def find_font_by_font_id(font_id):
    try:
        font = FontService().find_by_font_id(font_id).one()
        return jsonify(
            {
                "font_id": font.font_id,
                "channel_id": font.channel_id,
                "name": font.name,
                "team_id": font.team_id,
                "type": font.type
            }
        )

    except:
        return jsonify({"error": "Invalid Font request"})


@fonts_blueprint.route('/fonts/')
def find_fonts_by_request_parameter():
    response_data = []
    error1, error2 = False, False

    try:
        query_string = request.args.get('team_id')
        fonts = FontService().find_by_team_id(query_string)

        for font in fonts:
            response_data.append(
                {
                    "font_id": font.font_id,
                    "channel_id": font.channel_id,
                    "name": font.name,
                    "team_id": font.team_id,
                    "type": font.type
                }
            )

    except:
        error1 = True

    try:
        query_string = request.args.get('type')
        fonts = FontService().find_by_type(query_string)

        for font in fonts:
            font_data = {
                "font_id": font.font_id,
                "channel_id": font.channel_id,
                "name": font.name,
                "team_id": font.team_id,
                "type": font.type
            }

            if font_data not in response_data:
                response_data.append(font_data)
            else:
                continue

    except:
        error2 = True

    if error1 and error2:
        return jsonify({"error": "Invalid request"})
    else:
        return jsonify(response_data)


@fonts_blueprint.route('/fonts/new', methods=['POST'])
def add_new_font():
    request_data = request.json

    try:
        if request_data["token"] in UserService().find_by_user_id(
            request_data["user_id"].one().token
        ):
            new_font = FontService().add_new_font(
                channel_id=request_data["channel_id"],
                name=request_data["name"],
                type=request_data["team"]
            )

            github_consumer = GitHubConsumer(
                request_data["branch"],
                request_data["repository"],
                request_data["user"]
            )
            gh_files_list = github_consumer.list_contents(
                request_data["font_dir"]
            )

            for file in gh_files_list:
                if ".otf" in file or ".ttf" in file:
                    FontFaceService().add_new_font(
                        new_font.font_id,
                        (file.split(".")[0]).split("-")[1],
                        github_consumer.get_cdn_link(
                            request_data + "/" + file
                        )
                    )

            fontfaces = []

            for fontface in FontFaceService().find_by_font_id(new_font.font_id):
                fontfaces.append(
                    {
                        "fontface_id": fontface.fontface_id,
                        "fontface": fontface.fontface,
                        "resource_path": fontface.resource_path
                    }
                )

            new_role = RoleService().add_new(
                "font", new_font.font_id, "admin", request_data["user_id"]
            )

            return jsonify(
                {
                    "font_id": new_font.font_id,
                    "channel_id": new_font.channel_id,
                    "fontfaces": fontfaces,
                    "name": new_font.name,
                    "role_id": new_role.role_id,
                    "team_id": new_font.team_id,
                    "type": new_font.type
                }
            )

        else:
            return jsonify({"error": "Unauthorized request"})

    except:
        return jsonify({"error": "Error while creating new font"})


@fonts_blueprint.route('/fonts/<font_id>/update', methods=['POST'])
def update_font_by_font_id(font_id):
    request_data = request.json

    try:
        FontService().update_by_font_id(
            font_id,
            {
                "name": request_data["name"],
                "team_id": request_data["team_id"],
                "type": request_data["type"]
            }
        )
        font = FontService().find_by_font_id(font_id).one()

        return jsonify(
            {
                "font_id": font.font_id,
                "name": font.name,
                "team_id": font.team_id,
                "type": font.type
            }
        )

    except:
        return jsonify({"error": "Invalid request"})
