""" Rating

Rating and comments on users/teams/channels/fonts

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 31/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class Rating(Base):

    __tablename__ = 'rating'

    rating_id = Column(Integer, primary_key=True)
    comment = Column(String(250), nullable=True)
    entity = Column(String(20), nullable=False)
    entity_id = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    value = Column(Integer, default=0, nullable=False)
