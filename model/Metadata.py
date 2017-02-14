""" Metadata

Metdata of fonts.

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 15/2/2017
"""

from session import Base

from sqlalchemy import Column, ForeignKey, Integer, String


class Metadata(Base):

    __tablename__ = 'metadata'

    metadata_id = Column(Integer, primary_key=True)
    font_id = Column(Integer, ForeignKey("font.font_id"), nullable=False)
    default_fontface = Column(String(50), nullable=False)
    download_url = Column(String(200), nullable=True)
    license = Column(String(50), nullable=False)
    version = Column(String(20), nullable=True)
