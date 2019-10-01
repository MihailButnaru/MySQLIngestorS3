# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from src.config import Config
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

mysql_engine = create_engine(Config().DATABASE_CONNECTION)

# Session class created configured
Session = sessionmaker(bind=mysql_engine)

Base = declarative_base()

@contextmanager
def session_scope():
    """Provides a transactional scope around a series of operations. """
    session = Scope()
    Base.metadata.create_all(mysql_engine) # creates all the tables
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
