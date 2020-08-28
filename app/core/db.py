from functools import lru_cache
from typing import Any, Iterator

from fastapi_utils.camelcase import camel2snake
from fastapi_utils.session import FastAPISessionMaker
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from app.core.config import settings


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return camel2snake(cls.__name__)


engine = create_engine(settings.DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Iterator[Session]:
    """ FastAPI dependency that provides a sqlalchemy session """
    yield from _get_fastapi_sessionmaker().get_db()


@lru_cache()
def _get_fastapi_sessionmaker() -> FastAPISessionMaker:
    """ This function could be replaced with a global variable if preferred """
    database_uri = settings.database_uri
    return FastAPISessionMaker(database_uri)
