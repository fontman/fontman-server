""" subscriptions

User subscriptions

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from sqlalchemy import Column, Date, ForeignKey, Integer, String

from session import Base


class Subscription(Base):

    __tablename__ = 'subscription'

    id = Column(Integer, primary_key=True)
    current_revision = Column(String(20), nullable=False)
    end_date = Column(Date, nullable=True)
    font_id = Column(Integer, ForeignKey('font.font_id'), nullable=False)
    start_date = Column(Date, nullable=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
