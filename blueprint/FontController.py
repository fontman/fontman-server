""" Font controller

Manipulate font database, rest API

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 19/12/2016
"""

from flask import Blueprint, jsonify, request

from service import FontService, FontStyleService

font_blueprint = Blueprint('font_blueprint', __name__)


@font_blueprint.route('/font/add', methods=['POST'])
def add_new_font():
    font_data = request.json

    FontService().add_new(
        channel_id=font_data["channel_id"],
        name=font_data["name"],
        preview_cdn=font_data["preview_cdn"],
        sample=font_data["sample"],
        type=font_data["type"],
        version=font_data["version"],
        url=font_data["url"]
    )

    font = FontService().find_by_name(
        font_data["channel_id"],
        font_data["name"],
        font_data["url"]
    )

    return jsonify(
        {
            "font_id": font.id,
            "channel_id": font.channel_id,
            "name": font.name,
            "preview_cdn": font.preview_cdn,
            "sample": font.sample,
            "type": font.type,
            "url": font.url,
            "upgradable": font.upgradable,
            "version": font.version
        }
    )


@font_blueprint.route('/font/style/add', methods=['POST'])
def add_new_font_style():
    style_data = request.json
    FontStyleService().add_new(
        style_data["cdn"], style_data["font_id"], style_data["style"]
    )

    return jsonify(True)


@font_blueprint.route('/font/all', methods=['GET'])
def find_all_fonts():
    fonts_list = []

    for font in FontService().find_all():
        fonts_list.append(
            {
                "id": font.id,
                "channel_id": font.channel_id,
                "name": font.name,
                "preview_cdn": font.preview_cdn,
                "sample": font.sample,
                "type": font.type,
                "version": font.version,
                "url": font.url
            }
        )

    return jsonify(fonts_list)


@font_blueprint.route('/font/style/all')
def find_all_font_styles():
    styles_list = []

    for style in FontStyleService().find_all():
        styles_list.append(
            {
                "id": style.id,
                "cdn": style.cdn,
                "font_id": style.font_id,
                "style": style.style
            }
        )

    return jsonify(styles_list)


@font_blueprint.route('/font/style/all/<font_id>')
def find_styles_by_font_id(font_id):
    styles_list = []
    for style in FontStyleService().find_by_font_id(font_id):
        styles_list.append(
            {
                "id": style.id,
                "cdn": style.cdn,
                "font_id": style.font_id,
                "style": style.style
            }
        )

    return jsonify(styles_list)


@font_blueprint.route('/font/update', methods=['POST'])
def update_font():
    font_data = request.json

    FontService().update_by_id(
        font_data["font_id"],
        font_data["update_data"]
    )

    updated_font = FontService().find_by_id(font_data["id"])

    return jsonify(
        {
            "font_id": updated_font.id,
            "url": updated_font.url,
            "version": updated_font.version
        }
    )
