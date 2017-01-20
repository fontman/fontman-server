""" Font collections controller

REST blueprint to manipulate font collections database.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/1/2017
"""

from flask import Blueprint, jsonify, request

from consumer import GitHubConsumer
from service import FontFaceService
from service import FontService
from service import MetadataService
from service import RoleService
from service import UserService

fonts_blueprint = Blueprint("fonts_blueprint", __name__)


@fonts_blueprint.route("/fonts")
def find_all_fonts():
    response_data = []
    fonts = FontService().find_all()

    for font_id in fonts:
        response_data.append(font_id[0])

    return jsonify(response_data)


@fonts_blueprint.route("/fonts/<font_id>")
def find_font_by_font_id(font_id):
    try:
        font = FontService().find_by_font_id(font_id).one()
        return jsonify(
            {
                "font_id": font.font_id,
                "channel_id": font.channel_id,
                "name": font.name,
                "type": font.type
            }
        )

    except:
        return jsonify({"error": "Invalid Font request"})


@fonts_blueprint.route("/fonts/")
def find_fonts_by_request_parameter():
    response_data = []
    error = False

    try:
        query_string = request.args.get("type")
        fonts = FontService().find_by_type(query_string)

        for font in fonts:
            font_data = {
                "font_id": font.font_id,
                "channel_id": font.channel_id,
                "name": font.name,
                "type": font.type
            }

            if font_data not in response_data:
                response_data.append(font_data)
            else:
                continue

    except:
        error = True

    if error:
        return jsonify({"error": "Invalid request"})
    else:
        return jsonify(response_data)


@fonts_blueprint.route("/fonts/<font_id>/metadata")
def find_tags_url_by_font_id(font_id):
    try:
        metadata = MetadataService().find_by_font_id(font_id).first()
        consumer = GitHubConsumer(
            metadata.gh_pages_branch,
            metadata.git_repository,
            metadata.git_user
        )

        return jsonify(
            {
                "font_id": metadata.font_id,
                "tags_url": consumer.get_tags_url()
            }
        )

    except:
        return jsonify({"error": "Invalid request"})


@fonts_blueprint.route("/fonts/<font_id>/latest")
def find_latest_release_link_by(font_id):
    metadata = MetadataService().find_by_font_id(font_id).first()
    consumer = GitHubConsumer(
        metadata.gh_pages_branch,
        metadata.git_repository,
        metadata.git_user
    )

    return jsonify(
        {
            "font_id": font_id,
            "rel__info_url": consumer.get_release_info_url("latest")
        }
    )


@fonts_blueprint.route("/fonts/<font_id>/releases/<rel_id>")
def find_release_link_by_release_id(font_id, rel_id):
    metadata = MetadataService().find_by_font_id(font_id).first()
    consumer = GitHubConsumer(
        metadata.gh_pages_branch,
        metadata.git_repository,
        metadata.git_user
    )

    return jsonify(
        {
            "font_id": font_id,
            "rel_info_url": consumer.get_release_info_url(rel_id)
        }
    )


@fonts_blueprint.route("/fonts/new", methods=["POST"])
def add_new_font():
    request_data = request.json

    try:
        if request_data["token"] in UserService().find_by_user_id(
            request_data["user_id"]
        ).first().token:
            github_consumer = GitHubConsumer(
                request_data["ghPagesBranch"],
                request_data["gitRepository"],
                request_data["gitUser"]
            )
            gh_files_info_list = github_consumer.list_contents(
                request_data["ghPagesFontDir"]
            )

            new_font = FontService().add_new_font(
                request_data["channel_id"],
                request_data["name"],
                request_data["type"]
            )

            new_metadata = MetadataService().add_new(
                new_font.font_id,
                request_data["ghPagesBranch"],
                request_data["ghPagesFontDir"],
                request_data["gitRepository"],
                request_data["gitUser"]
            )

            for file_info in gh_files_info_list:
                print(gh_files_info_list)
                if "test" in (file_info["name"]).lower():
                    continue

                if ".otf" in file_info["name"] or ".ttf" in file_info["name"]:
                    FontFaceService().add_new_font(
                        new_font.font_id,
                        (file_info["name"].split(".")[0]).split("-")[1],
                        github_consumer.get_cdn_link(file_info["path"])
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
                    "type": new_font.type
                }
            )

        else:
            return jsonify({"error": "Unauthorized request"})

    except:
        return jsonify({"error": "Invalid data provided. Please check."})


@fonts_blueprint.route("/fonts/<font_id>/update", methods=["POST"])
def update_font_by_font_id(font_id):
    request_data = request.json

    try:
        FontService().update_by_font_id(
            font_id,
            {
                "name": request_data["name"],
                "type": request_data["type"]
            }
        )
        font = FontService().find_by_font_id(font_id).one()

        return jsonify(
            {
                "font_id": font.font_id,
                "name": font.name,
                "type": font.type
            }
        )

    except:
        return jsonify({"error": "Invalid request"})
