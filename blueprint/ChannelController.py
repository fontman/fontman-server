""" Channel controller

CRUD operations and permission set on channels.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 19/12/2016
"""

from flask import Blueprint, jsonify, request

from service import ChannelService, FontService

channel_blueprint = Blueprint('channel_blueprint', __name__)


@channel_blueprint.route('/channel/add', methods=['POST'])
def add_new_channel():
    channel_data = request.json

    ChannelService().add_new(
        key=channel_data["key"],
        name=channel_data["name"],
        type=channel_data["type"]
    )

    channel = ChannelService().find_by_details(
        channel_data["key"], channel_data["name"], channel_data["type"]
    )

    response_data = {
        "channel_id": channel["id"],
        "key": channel["key"],
        "name": channel["name"],
        "type": channel["type"]
    }

    return jsonify(response_data)


@channel_blueprint.route('/channel/all', methods=['GET'])
def find_all_channels():
    channels_list = []

    for channel in ChannelService().find_all():
        channels_list.append(
            {
                "channel_id": channel.id,
                "name": channel.name,
                "type": channel.type
            }
        )

    return jsonify(channels_list)


@channel_blueprint.route('/channel/fonts/<id>')
def find_fonts_by_channel_id(id):
    fonts_list = []

    for font in FontService().find_all_by_channel_id(id):
        fonts_list.append(
            {
                "id": font.id,
                "cdn": font.preview_cdn,
                "channel_id": font.channel_id,
                "name": font.name,
                "version": font.version
            }
        )

    return jsonify(fonts_list)


@channel_blueprint.route('/channel/find/<id>', methods=['GET'])
def find_by_channel_id(id):
    channel = ChannelService().find_by_id(id).one()

    return jsonify({
        "id": channel.id,
        "name": channel.name,
        "type": channel.type
    })
