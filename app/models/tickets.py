from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import TEXT
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class TicketsStatus(Enum):
    open: str = "open"
    answered: str = "answered"
    waiting_for_answer: str = "waiting_for_answer"
    closed: str = "closed"


class Tickets(Base):
    __tablename__ = "tickets"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    creation_date: Mapped[datetime]
    modification_date: Mapped[datetime]
    topic_name: Mapped[str]
    text: Mapped[str] = mapped_column(TEXT)
    email: Mapped[str]
    status: Mapped[TicketsStatus]
