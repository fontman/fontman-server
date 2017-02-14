""" Collection

Font collections model. Table for curated and standard font collections.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/1/2016
"""

from session import Base

from sqlalchemy import Column, ForeignKey, Integer, String


class Collection(Base):

    __tablename__ = 'collection'

    collection_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(20), default='curated', nullable=False)
