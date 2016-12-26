""" Languages controller

CRUD operations on languages.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 23/12/2016
"""

from flask import Blueprint, jsonify

from service import FontLanguageService, LanguageService

language_blueprint = Blueprint('language_blueprint', __name__)


@language_blueprint.route('/language/all')
def find_all_languages():
    languages_list = []

    for language in LanguageService().find_all():
        languages_list.append(
            {
                "language_id": language.id,
                "value": language.value
            }
        )

    return jsonify(languages_list)


@language_blueprint.route('/language/font/all')
def find_all_font_languages():
    font_languages = []

    for font_language in FontLanguageService().find_all():
        font_languages.append(
            {
                "id": font_language.id,
                "font_id": font_language.font_id,
                "language_id": font_language.language_id
            }
        )

    return jsonify(font_languages)
