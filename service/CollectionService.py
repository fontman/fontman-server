""" Collections service

Provides high level functions to manipulate font collections table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/2/2017
"""

from model import Collection
from session import DBSession


class CollectionService:

    def __init__(self):
        self.__db_session = DBSession()

    def add_new(self, name, type):
        new_collection = Collection(
            name=name,
            type=type
        )

        self.__db_session.add(new_collection)
        self.__db_session.commit()

        return new_collection

    def delete_by_collection_id(self, collection_id):
        self.find_by_collection_id(collection_id).delete()
        self.__db_session.commit()

    def find_all(self):
        return self.__db_session.query(Collection.collection_id)

    def find_by_collection_id(self, collection_id):
        return self.__db_session.query(Collection).filter_by(
            collection_id=collection_id
        )

    def find_by_type(self, type):
        return self.__db_session.query(Collection).filter_by(type=type)

    def update_by_collection_id(self, collection_id, update_data):
        self.find_by_collection_id(collection_id).update(update_data)
        self.__db_session.commit()
