""" Font service

Provides high level functions to manipulate font database

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 19/12/2016
"""

from model import Font
from session import db_session


class FontService:

    def add_new(
            self, channel_id, name, preview_cdn, sample, type, version, url
    ):
        new_font = Font(
            channel_id=channel_id,
            name=name,
            preview_cdn=preview_cdn,
            sample=sample,
            type=type,
            version=version,
            url=url
        )

        db_session.add(new_font)
        db_session.commit()

    def delete_by_id(self, id):
        self.find_by_id(id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(Font).all()

    def find_all_by_channel_id(self, channel_id):
        return db_session.query(Font).filter_by(channel_id=channel_id).all()

    def find_by_id(self, id):
        return db_session.query(Font).filter_by(id=id)

    def find_by_name(self, channel_id, name, url):
        return db_session.query(Font).filter_by(
            channel_id=channel_id, name=name, url=url
        )

    def update_by_id(self, id, update_list):
        self.find_by_id(id).update(update_list)
        db_session.commit()
