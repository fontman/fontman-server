""" Channel

Broadcast fonts through channels, users can request channels.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""


from sqlalchemy import Column, Integer, String

from session import Base


class Channel(Base):

    __tablename__ = 'channel'

    id = Column(Integer, primary_key=True)
    key = Column(String(200), nullable=False)
    name = Column(String(100), nullable=False)
    type = Column(String(20), default='public', nullable=False)
