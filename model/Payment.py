""" payments

user payment

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

from sqlalchemy import Column, Float, ForeignKey, Integer

from session import Base


class Payment(Base):

    __tablename__ = 'payment'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    amount = Column(Float(50), nullable=False)
