""" Fonts

Contains basic information of fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from session import Base

from sqlalchemy import Column, ForeignKey, Integer, String


class Font(Base):

    __tablename__ = 'font'

    font_id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey('channel.channel_id'))
    name = Column(String(100), nullable=False)
    type = Column(String(20), default='public', nullable=False)
