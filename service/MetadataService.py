""" Metadata service

Provides high level functions to manipulate metadata table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from model import Metadata
from session import db_session


class MetadataService:

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

        db_session.add(new_metadata)
        db_session.commit()

        return new_metadata

    def delete_by_font_id(self, font_id):
        self.find_by_font_id(font_id).delete()
        db_session.commit()

    def find_by_font_id(self, font_id):
        return db_session.query(Metadata).filter_by(font_id=font_id)

    def update_by_key(self, font_id, update_data):
        self.find_by_font_id(font_id).update(update_data)
        db_session.commit()
