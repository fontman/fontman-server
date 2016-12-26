""" Users

Fontman users

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

from sqlalchemy import Column, Integer, String

from session import Base


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    key = Column(String(200), nullable=False)
    name = Column(String(200), nullable=False)
    secret = Column(String(250), nullable=False)
