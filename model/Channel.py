""" Channel

Channel Entity.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from session import Base

from sqlalchemy import Column, Integer, String


class Channel(Base):

    __tablename__  = "channel"

    channel_id = Column(Integer, primary_key=True)
    maintainer_id = Column(Integer, nullable=True)
    name = Column(String(100), nullable=False)
    type = Column(String(20), default="public", nullable=False)
