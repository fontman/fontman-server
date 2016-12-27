""" Tag

Tags for fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class Tag(Base):

    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    font_id = Column(Integer, ForeignKey('font.font_id'), nullable=False)
    tag = Column(String(100), nullable=False)
