""" Font collection service

Provides high level functions to manipulate font_collection table data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/1/2017
"""

from model import FontCollection
from session import DBSession


class FontCollectionService:
    
    def __init__(self):
        self.__db_session = DBSession()

    def add_new(self, collection_id, font_id):
        new_font_collection = FontCollection(
            collection_id=collection_id,
            font_id=font_id
        )

        self.__db_session.add(new_font_collection)
        self.__db_session.commit()

        return new_font_collection

    def delete_by_font_collection_id(self, font_collection_id):
        self.find_by_font_collection_id(font_collection_id).delete()

    def find_by_font_collection_id(self, font_collection_id):
        return self.__db_session.query(FontCollection).filter_by(
            font_collection_id=font_collection_id
        )

    def find_by_collection_id(self, collection_id):
        return self.__db_session.query(FontCollection).filter_by(
            collection_id=collection_id
        )

    def find_by_font_id(self, font_id):
        return self.__db_session.query(FontCollection).filter_by(
            font_id=font_id
        )
