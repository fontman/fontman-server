""" Tags service

High level functions to manipulate tags table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/1/2017
"""

from model import Tag
from session import DBSession


class TagService:

    def __init__(self):
        self.__db_session = DBSession()

    def add_new(self, font_id, key, value):
        new_tag = Tag(
            font_id=font_id,
            key = key,
            value=value
        )

        self.__db_session.add(new_tag)
        self.__db_session.commit()

        return new_tag

    def delete_by_font_id(self, font_id):
        self.find_by_font_id(font_id).delete()
        self.__db_session.commit()

    def find_by_font_id(self, font_id):
        return self.__db_session.query(Tag).filter_by(font_id=font_id)

    def find_by_key(self,key):
        return self.__db_session.query(Tag).filter_by(key=key)

    def find_by_tag_id(self, tag_id):
        return self.__db_session.query(Tag).filter_by(tag_id=tag_id)

    def find_by_value(self, value):
        return self.__db_session.query(Tag).filter_by(value=value)

    def find_by_key_value(self, key, value):
        return self.__db_session.query(Tag).filter_by(key=key, value=value)

    def update_by_font_id(self, tag_id, update_data):
        self.find_by_tag_id(tag_id).update(update_data)
        self.__db_session.commit()
