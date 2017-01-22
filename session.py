""" session

Session variables and functions.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# fontman version
version = '0.1.0-SNAPSHOT'

# API version and route URL
application_root = "/api/v1alpha"

# mysql con string
mysql_con_string = "mysql://root@localhost/fontman?charset=utf8"

# Database session variables
engine = create_engine(
    mysql_con_string,
    isolation_level="READ UNCOMMITTED",
    poolclass=StaticPool,
    echo=True
)
Base = declarative_base()

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

db_session = DBSession()
