""" Role

Defines user roles.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 31/12/2016
"""

from sqlalchemy import Column, Float, ForeignKey, Integer, String

from session import Base


class Role(Base):

    __tablename__ = 'role'

    role_id = Column(Integer, primary_key=True)
    entity = Column(String(20), nullable=False)
    entity_id = Column(Integer, nullable=False)
    role = Column(String(20), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
