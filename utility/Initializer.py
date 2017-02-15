""" Initializer

Initialize application data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 19/12/2016
"""

from session import Base
from session import mysql_con_string

from sqlalchemy import create_engine

from utility import DBManager


def initialize():
    engine = create_engine(
        mysql_con_string
    )
    Base.metadata.create_all(engine, checkfirst=True)
    DBManager().update_font_cache()
