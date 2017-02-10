""" Font collections controller

REST blueprint to manipulate font collections database.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/1/2017
"""

from flask import Blueprint, jsonify, request

from consumer import GitHubConsumer
from service import FontService
from service import MetadataService

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
                "latest_tag_url": consumer.get_release_info_url("latest"),
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
            "rel_info_url": consumer.get_release_info_url("latest")
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
