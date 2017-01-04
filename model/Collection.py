""" Collection

Font collections model. Table for curated and standard font collections.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/1/2016
"""

from sqlalchemy import Column, ForeignKey, Float, Integer, String

from session import Base


class Collection(Base):

    __tablename__ = 'collection'

    collection_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(20), default='public', nullable=False)
    team_id = Column(Integer, ForeignKey('user.use_id'), nullable=False)
