""" Font style service

Provides high level functions to manipulate font styles

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 20/12/2016
"""

from model import FontStyle
from session import db_session


class FontStyleService:

    def add_new(self, cdn, font_id, style):
        new_font_style = FontStyle(
            cdn=cdn,
            font_id=font_id,
            style=style
        )

        db_session.add(new_font_style)
        db_session.commit()

    def delete_by_font_id(self, font_id):
        self.delete_by_font_id(font_id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(FontStyle).all()

    def find_by_font_id(self, font_id):
        return db_session.query(FontStyle).filter_by(font_id=font_id).all()

    def find_by_id(self, id):
        return db_session.query(FontStyle).filter_by(id=id)

    def update_by_id(self, id, update_list):
        self.find_by_id(id).update(update_list)
        db_session.commit()
