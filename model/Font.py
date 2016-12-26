""" Fonts

Font information

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""


from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class Font(Base):

    __tablename__ = 'font'

    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey("channel.id"), nullable=False)
    name = Column(String(200), nullable=False)
    preview_cdn = Column(String(250), nullable=False)
    sample = Column(String(250), nullable=False)
    type = Column(String(20), nullable=False)
    url = Column(String(250), nullable=False)
    version = Column(String(50), nullable=False)
