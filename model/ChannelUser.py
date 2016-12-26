""" Channel users

User access levels to channels.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from session import Base


class ChannelUser(Base):

    __tablename__ = 'channel_user'

    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey('channel.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
