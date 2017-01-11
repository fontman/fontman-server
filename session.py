""" session

Session variables and functions.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# fontman version
version = '0.0.1-SNAPSHOT'

# API version and route URL
application_root = "/api/v1alpha"

# Database session variables
engine = create_engine(
    "mysql://root:password@localhost/fontman?charset=utf8",
    isolation_level="READ UNCOMMITTED",
    poolclass=StaticPool,
    echo=True
)
Base = declarative_base()

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

db_session = DBSession()
