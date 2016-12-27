""" Metadata service

Provides high level functions to manipulate metadata table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from model import Metadata
from session import db_session


class MetadataService:

    def add_new(self, font_id, key, value):
        new_metadata = Metadata(font_id=font_id, key=key, value=value)

        db_session.add(new_metadata)
        db_session.commit()

    def delete_by_font_id(self, font_id):
        self.find_by_font_id(font_id).delete()
        db_session.commit()

    def delete_by_key(self, font_id, key):
        self.find_by_key(font_id, key).delete()
        db_session.commit()

    def find_by_font_id(self, font_id):
        return db_session.query(Metadata).filter_by(font_id=font_id)

    def find_by_key(self, font_id, key):
        return db_session.query(Metadata).filter_by(font_id=font_id, key=key)

    def update_by_key(self, font_id, key, update_data):
        self.find_by_key(font_id, key).update(update_data)
        db_session.commit()
