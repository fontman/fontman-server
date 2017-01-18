""" Metadata

Contains information about metadata of fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class Metadata(Base):

    __tablename__ = 'metadata'

    metadata_id = Column(Integer, primary_key=True)
    font_id = Column(Integer, ForeignKey('font.font_id'), nullable=False)
    gh_pages_branch = Column(String(50), nullable=False)
    gh_pages_font_dir = Column(String(50), nullable=False)
    git_repository = Column(String(50), nullable=False)
    git_user = Column(String(50), nullable=False)
