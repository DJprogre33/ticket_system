from datetime import datetime
from enum import Enum

from app.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from marshmallow.validate import Email


class TicketsStatus(Enum):
    OPEN: str = "open"
    ANSWERED: str = "answered"
    WAITING_FOR_ANSWER = "waiting for answer"
    CLOSED: str = "closed"


class Tickets(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    creation_date: Mapped[datetime]
    modification_date: Mapped[datetime]
    topic_name: Mapped[str]
    email: Mapped[Email]
    status: Mapped[TicketsStatus]


