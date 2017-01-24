""" Font service

REST blueprint to manipulate font table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/1/2017
"""

from model import Font
from session import DBSession


class FontService:
    
    def __init__(self):
        self.__db_session = DBSession()

    def add_new_font(self, channel_id, name, type):
        new_font = Font(
            channel_id=channel_id,
            name=name,
            type=type
        )

        self.__db_session.add(new_font)
        self.__db_session.commit()

        return new_font

    def delete_by_font_id(self, font_id):
        self.find_by_font_id(font_id).delete()
        self.__db_session.commit()

    def find_all(self):
        return self.__db_session.query(Font.font_id)

    def find_by_channel_id(self, channel_id):
        return self.__db_session.query(Font).filter_by(channel_id=channel_id)

    def find_by_font_id(self, font_id):
        return self.__db_session.query(Font).filter_by(font_id=font_id)

    def find_by_team_id(self, team_id):
        return self.__db_session.query(Font).filter_by(team_id=team_id)

    def find_by_type(self, type):
        return self.__db_session.query(Font).filter_by(type=type)

    def update_by_font_id(self, font_id, update_data):
        self.find_by_font_id(font_id).update_data(update_data)
        self.__db_session.commit()
