""" Font service

Provides high level functions to manipulate font table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 19/12/2016
"""

from model import Font
from session import db_session


class FontService:

    def add_new(
            self, font_id, download_url, name, price, version
    ):
        new_font = Font(
            font_id=font_id,
            download_url=download_url,
            name=name,
            price=price,
            version=version
        )

        db_session.add(new_font)
        db_session.commit()

    def delete_by_font_id(self, font_id):
        self.find_by_font_id(font_id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(Font).all()

    def find_by_font_id(self, font_id):
        return db_session.query(Font).filter_by(font_id=font_id)

    def update_by_id(self, font_id, update_data):
        self.find_by_font_id(font_id).update(update_data)
        db_session.commit()
