from datetime import UTC, datetime
from uuid import UUID

from sqlalchemy.orm import Session
from werkzeug.exceptions import NotFound

from app.models.comments import Comments
from app.repositories.comments import CommentsRepository
from app.repositories.tickets import TicketsRepository


class CommentsService:
    @staticmethod
    def create_new_comment(
        db: Session, ticket_id: UUID, author_email: str, text: str
    ) -> Comments:
        current_date = datetime.now(tz=UTC)
        tickets_repo, comments_repo = TicketsRepository(db), CommentsRepository(db)

        existing_ticket = tickets_repo.find_one_or_none(id=ticket_id)
        if not existing_ticket:
            raise NotFound("Incorrect ticket id")

        created_comment = comments_repo.insert_data(
            ticket_id=ticket_id,
            creation_date=current_date,
            author_email=author_email,
            text=text,
        )
        return created_comment
