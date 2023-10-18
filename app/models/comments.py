from datetime import datetime

from app.db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy import ForeignKey
from marshmallow.validate import Email


class Comments(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    ticket_id: Mapped[int] = mapped_column(ForeignKey("tickets.id", ondelete="CASCADE"))
    creation_date: Mapped[datetime]
    author_email: Mapped[Email]
    text: Mapped[TEXT]