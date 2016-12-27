""" Fonts

Contains basic information of fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""


from sqlalchemy import Column, Float, Integer, String

from session import Base


class Font(Base):

    __tablename__ = 'font'

    font_id = Column(Integer, primary_key=True)
    download_url = Column(String(250), nullable=False)
    name = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    version = Column(String(50), nullable=False)
