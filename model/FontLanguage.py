""" Font language

Keep language information of fonts

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer

from session import Base


class FontLanguage(Base):

    __tablename__ = "font_language"

    id = Column(Integer, primary_key=True)
    font_id = Column(Integer, ForeignKey("font.id"), nullable=False)
    language_id = Column(Integer, ForeignKey("language.id"), nullable=False)
