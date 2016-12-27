""" Tag service

Provides high level functions to manipulate tags table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

from model import Tag
from session import db_session


class TagService:

    def add_new(self, font_id, tag):
        new_tag = Tag(font_id=font_id, tag=tag)

        db_session.add(new_tag)
        db_session.commit()

    def delete_by_font_id(self, font_id):
        self.find_by_font_id(font_id).delete()
        db_session.commit()

    def delete_by_id(self, id):
        self.find_by_id(id).delete()
        db_session.commit()

    def delete_tag(self, font_id, tag):
        self.find_tag(font_id, tag).delete()
        db_session.commit()

    def find_by_font_id(self, font_id):
        return db_session.query(Tag).filter_by(font_id=font_id)

    def find_by_id(self, id):
        return db_session.query(Tag).filter_by(id=id)

    def find_tag(self, font_id, tag):
        return db_session.query(Tag).filter_by(font_id=font_id, tag=tag)

    def update_by_id(self, id, update_data):
        self.find_by_id(id).update(update_data)
        db_session.commit()
