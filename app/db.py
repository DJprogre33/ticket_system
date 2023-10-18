from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from app.config import settings


engine = create_engine(settings.database_url, echo=True)
session = sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
