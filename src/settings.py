import logging
from typing import Optional

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session as SASession

from src.configuration import conf
from src.sql.base import Base

log = logging.getLogger(__name__)

CONFIG_PATH = ""
LOGGING_LEVEL = conf.read("logging", "level")
LOGGING_FORMAT = conf.read("logging", "format")

engine: Optional[Engine] = None
Session: Optional[SASession] = None

DB_URL = conf.get('database', "db_url")


def create_conn():
    global engine
    log.debug(f"DB_URL {DB_URL}")
    if DB_URL is not None:
        engine = create_engine(DB_URL)
        log.info("Engine created")
        return engine


def create_session():
    """Create session with database"""
    global engine
    engine = create_conn()

    # create all objects ??
    Base.metadata.create_all(engine)

    # create session to handle db objects
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def dispose():
    """Close connection to database"""
    global Session
    global engine
    if Session:
        Session.remove()
        Session = None
    if engine:
        engine.dispose()
        engine = None
