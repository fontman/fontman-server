""" Users

Fontman user data table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from sqlalchemy import Column, Integer, String

from session import Base


class User(Base):

    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    name = Column(String(200), nullable=False)
    password = Column(String(250), nullable=False)
    username = Column(String(200), nullable=False)
