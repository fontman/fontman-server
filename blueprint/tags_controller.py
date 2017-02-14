""" Tags controller

REST blueprint for font tags.

Created by Lahiru Pathirage @ Mooniak <lpsandaruwan@gmail.com> on 8/2/2017
"""

from service import TagService

from flask import Blueprint, jsonify

tags_blueprint = Blueprint("tags_blueprint", __name__)


@tags_blueprint.route("/tags/<font_id>")
def find_tags_by_font_id(font_id):
    response_data = []
    tags = TagService().find_by_font_id(font_id)

    for tag in tags:
        response_data.append(
            {
                "tag_id": tag.tag_id,
                "font_id": tag.font_id,
                "key": tag.key,
                "value": tag.value
            }
        )

    return jsonify(response_data)
