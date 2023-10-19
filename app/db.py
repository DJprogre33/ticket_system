from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, scoped_session, sessionmaker

from app.config import settings

engine = create_engine(settings.database_url, echo=False)
SessionFactory = sessionmaker(bind=engine, expire_on_commit=False)
db_session = scoped_session(SessionFactory)


class Base(DeclarativeBase):
    pass


def init_db():
    from app.models.comments import Comments
    from app.models.tickets import Tickets

    Base.metadata.create_all(bind=engine)
