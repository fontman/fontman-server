""" Metadata service

High level functions to manipulate metadata table.

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 3/1/2017
"""

from model import Metadata
from session import DBSession


class MetadataService:
    def __init__(self):
        self.__db_session = DBSession()

    def add_new_metadata(
            self,
            font_id,
            default_fontface,
            download_url,
            license,
            version
    ):
        new_metadata = Metadata(
            font_id=font_id,
            default_fontface=default_fontface,
            download_url=download_url,
            license=license,
            version=version
        )

        self.__db_session.add(new_metadata)
        self.__db_session.commit()

        return new_metadata

    def delete_by_metadata_id(self, metadata_id):
        self.find_by_font_id(metadata_id).delete()
        self.__db_session.commit()

    def find_all(self):
        return self.__db_session.query(Metadata)

    def find_by_font_id(self, font_id):
        return self.__db_session.query(Metadata).filter_by(
            font_id=font_id
        )

    def update_by_font_id(self, font_id, update_data):
        self.find_by_font_id(font_id).update_data(update_data)
        self.__db_session.commit()
