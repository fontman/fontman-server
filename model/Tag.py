""" Tag

Keeps tags on more information of fonts.
Eg: languages, serif/sans-serif...

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 8/2/2017
"""

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy import String

from session import Base


class Tag(Base):

    __tablename__ = "tag"

    tag_id = Column(Integer, primary_key=True)
    font_id = Column(Integer, ForeignKey("font.font_id"), nullable=False)
    key = Column(String(20), nullable=False)
    value = Column(String(20), nullable=False)
