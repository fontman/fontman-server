""" Fonts

Contains basic information of fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from session import Base

from sqlalchemy import Column, Integer, String


class Font(Base):

    __tablename__ = 'font'

    font_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
