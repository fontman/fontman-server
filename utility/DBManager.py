""" Database manager

CRUD on MySQL database, using font index repository.

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 14/02/2017
"""

from consumer import FontIndexConsumer
from service import FontFaceService
from service import FontService
from service import MetadataService
from service import TagService


class DBManager:

    def update_font_cache(self):
        font_list = FontService().find_all()
        index_data = FontIndexConsumer().load_font_index()

        for element in index_data:
            trigger = False
            
            for font in font_list:
                if font.name == element["name"]:
                    update_data = {
                        "download_url": element["download_url"],
                        "version": element["version"]
                    }

                    MetadataService().update_by_font_id(
                        font.font_id, update_data
                    )

                    trigger = True
                    break

            if trigger:
                continue

            new_font = FontService().add_new_font(element["name"])
            MetadataService().add_new_metadata(
                new_font.font_id,
                element["default_fontface"],
                element["download_url"],
                element["license"],
                element["version"]
            )

            for fontface in element["fontfaces"].keys():
                FontFaceService().add_new_font(
                    new_font.font_id,
                    fontface,
                    element["fontfaces"][fontface]
                )

            for language in element["languages"]:
                TagService().add_new(
                    new_font.font_id,
                    "languages",
                    language
                )
