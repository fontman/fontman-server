""" Initializer

Initialize application data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 19/12/2016
"""

from sqlalchemy import create_engine

from session import Base


def Initialize():
    engine = create_engine(
        "mysql://root:root@localhost/fontman"
    )
    Base.metadata.create_all(engine)
