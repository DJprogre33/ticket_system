from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Comments(Base):
    __tablename__ = "comments"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    ticket_id: Mapped[int] = mapped_column(ForeignKey("tickets.id", ondelete="CASCADE"))
    creation_date: Mapped[datetime]
    author_email: Mapped[str]
    text: Mapped[str] = mapped_column(TEXT)
