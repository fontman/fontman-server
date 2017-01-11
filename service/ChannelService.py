""" Channel service

High level functions to manipulate channels table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 31/12/2016
"""

from session import db_session
from model import Channel


class ChannelService:

    def find_all(self):
        return db_session.query(Channel).all()
