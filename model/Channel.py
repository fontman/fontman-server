""" Channel

Channel Entity.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from sqlalchemy import Column, ForeignKey, Float, Integer, String

from session import Base


class Channel(Base):

    __tablename__  = 'channel'

    channel_id = Column(Integer, primary_key=True)
    maintainer_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    name = Column(String(100), nullable=False)
    type = Column(String(20), default='public', nullable=False)
