from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from src.config import DB_HOST, DB_NAME, DB_PASS, DB_USER, DB_PORT

Base: DeclarativeMeta = declarative_base()

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(DATABASE_URL, echo=True)

session_maker = sessionmaker(bind=engine)


def get_session() -> Session:
    session = session_maker()
    return session
