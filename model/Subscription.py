""" subscriptions

user subscriptions

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class Subscription(Base):

    __tablename__ = 'subscription'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True, primary_key=True)
