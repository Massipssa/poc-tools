from sqlalchemy.orm.session import Session as SASession
from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker
from sql.base import Base
from typing import Optional
from aws.configuration import config
import logging

log = logging.getLogger(__name__)

engine: Optional[Engine] = None
Session: Optional[SASession] = None

DB_URL = config.get('database', "db_url")


def create_conn():
    global engine
    log.debug("DB_URL %s".format(DB_URL))
    if DB_URL is not None:
        engine = create_engine(DB_URL)
        log.info("Engine created")
        return engine


def create_session():

    global engine
    engine = create_conn()

    # create all objects ??
    Base.metadata.create_all(engine)

    # create session to handle db objects
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def dispose():
    global Session
    global engine
    if Session:
        Session.remove()
        Session = None
    if engine:
        engine.dispose()
        engine = None
