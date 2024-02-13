import os

from sqlmodel import create_engine, SQLModel, Session

from .config import settings

if settings.MODE == "TEST":
    DATABASE_URL = settings.DATABASE_URL_TEST
else:
    DATABASE_URL = settings.DATABASE_URL

engine = create_engine(settings.DATABASE_URL, echo=True, future=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
