""" Fonts

Contains basic information of fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class Font(Base):

    __tablename__ = 'font'

    font_id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey('channel.channel_id'))
    name = Column(String(100), nullable=False)
    team_id = Column(Integer, ForeignKey('team.team_id'), nullable=False)
    type = Column(String(20), default='public', nullable=False)
