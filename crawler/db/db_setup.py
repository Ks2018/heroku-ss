from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'russell',
    'password': '',
    'database': 'subtitledscreenings'
}

engine = create_engine(URL(**DATABASE), convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()

Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
