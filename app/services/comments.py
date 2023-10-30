from datetime import UTC, datetime
from uuid import UUID

from sqlalchemy.orm import Session
from werkzeug.exceptions import NotFound

from app.models.comments import Comments
from app.repositories.comments import CommentsRepository
from app.repositories.tickets import TicketsRepository


class CommentsService:
    def __init__(self, db: Session):
        self.tickets_repo = TicketsRepository(db)
        self.comments_repo = CommentsRepository(db)

    def create_new_comment(
        self, ticket_id: UUID, author_email: str, text: str
    ) -> Comments:
        current_date = datetime.now(tz=UTC)

        existing_ticket = self.tickets_repo.find_one_or_none(id=ticket_id)
        if not existing_ticket:
            raise NotFound("Incorrect ticket id")

        created_comment = self.comments_repo.insert_data(
            ticket_id=ticket_id,
            creation_date=current_date,
            author_email=author_email,
            text=text,
        )
        self.comments_repo.commit()
        return created_comment
