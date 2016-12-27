""" Metadata

Contains information about metadata of fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class Metadata(Base):

    __tablename__ = 'metadata'

    id = Column(Integer, primary_key=True)
    font_id = Column(Integer, ForeignKey('font.font_id'), nullable=False)
    key = Column(String(100), nullable=False)
    value = Column(String(250), nullable=False)
