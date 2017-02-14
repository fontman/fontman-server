""" Font-faces service

High level functions to manipulate font faces table.

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 4/1/2017
"""

from model import FontFace
from session import DBSession


class FontFaceService:
    
    def __init__(self):
        self.__db_session = DBSession()

    def add_new_font(self, font_id, fontface, resource_path):
        new_fontface = FontFace(
            font_id=font_id,
            fontface=fontface,
            resource_path=resource_path
        )

        self.__db_session.add(new_fontface)
        self.__db_session.commit()

        return new_fontface

    def delete_by_fontface_id(self, fontface_id):
        self.find_by_fontface_id(fontface_id).delete()
        self.__db_session.commit()

    def find_all(self):
        return self.__db_session.query(FontFace.fontface_id)

    def find_by_fontface_id(self, fontface_id):
        return self.__db_session.query(FontFace).filter_by(
            fontface_id=fontface_id
        )

    def find_by_font_id(self, font_id):
        return self.__db_session.query(FontFace).filter_by(font_id=font_id)

    def update_by_fontface_id(self, fontface_id, update_data):
        self.find_by_fontface_id(fontface_id).update(update_data)
        self.__db_session.commit()
