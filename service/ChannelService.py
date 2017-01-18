""" Channel service

High level functions to manipulate channels table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 31/12/2016
"""

from session import db_session
from model import Channel


class ChannelService:

    def add_new(self, name, type, maintainer_id=0):
        new_channel = Channel(
            maintainer_id=maintainer_id,
            name=name,
            type=type
        )

        db_session.add(new_channel)
        db_session.commit()

        return new_channel

    def find_all(self):
        return db_session.query(Channel.channel_id)

    def find_by_channel_id(self, channel_id):
        return db_session.query(Channel).filter_by(channel_id=channel_id)
