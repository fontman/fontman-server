""" Channels controller

REST blueprint to provide channel API

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 9/1/2017
"""

from service import ChannelService

from flask import Blueprint, jsonify

channels_blueprint = Blueprint("channels_blueprint", __name__)


@channels_blueprint.route("/channels")
def find_all_channels():
    response = []

    for channel_id in ChannelService().find_all():
        response.append(channel_id[0])

    return jsonify(response)


@channels_blueprint.route("/channels/<channel_id>")
def find_by_font_id(channel_id):
    channel = ChannelService().find_by_channel_id(channel_id).first()

    return jsonify(
        {
            "channel_id": channel.channel_id,
            "name": channel.name,
            "type": channel.type
        }
    )
