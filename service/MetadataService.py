""" Metadata service

Provides high level functions to manipulate metadata table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from model import Metadata
from session import DBSession


class MetadataService:
    def __init__(self):
        self.__db_session = DBSession()
    

    def add_new(
            self,
            font_id,
            gh_pages_branch,
            gh_pages_font_dir,
            git_repository,
            git_user
    ):
        new_metadata = Metadata(
            font_id=font_id,
            gh_pages_branch=gh_pages_branch,
            gh_pages_font_dir=gh_pages_font_dir,
            git_repository=git_repository,
            git_user=git_user
        )

        self.__db_session.add(new_metadata)
        self.__db_session.commit()

        return new_metadata

    def delete_by_font_id(self, font_id):
        self.find_by_font_id(font_id).delete()
        self.__db_session.commit()

    def find_by_font_id(self, font_id):
        return self.__db_session.query(Metadata).filter_by(font_id=font_id)

    def update_by_key(self, font_id, update_data):
        self.find_by_font_id(font_id).update(update_data)
        self.__db_session.commit()
