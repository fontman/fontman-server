""" Font collections controller

REST blueprint to manipulate font collections database.

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 3/1/2017
"""

from service import FontService
from service import MetadataService

from flask import Blueprint, jsonify

fonts_blueprint = Blueprint("fonts_blueprint", __name__)


@fonts_blueprint.route("/fonts")
def find_all_fonts():
    response_data = []
    fonts = FontService().find_all()

    for font in fonts:
        response_data.append(font.font_id)

    return jsonify(response_data)


@fonts_blueprint.route("/fonts/<font_id>")
def find_font_by_font_id(font_id):
    font_data = FontService().find_by_font_id(font_id).first()
    metadata = MetadataService().find_by_font_id(font_id).first()

    if font_data is None:
        return jsonify({"error": "Invalid request"})

    return jsonify(
        {
            "font_id": font_data.font_id,
            "default_fontface": metadata.default_fontface,
            "download_url": metadata.download_url,
            "license": metadata.license,
            "metadata_id": metadata.metadata_id,
            "name": font_data.name,
            "version": metadata.version
        }
    )
