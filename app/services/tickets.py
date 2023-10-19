from datetime import UTC, datetime
from uuid import UUID

from sqlalchemy.orm import Session
from werkzeug.exceptions import BadRequest, NotFound

from app.models.tickets import Tickets, TicketsStatus
from app.repositories.tickets import TicketsRepository


class TicketsService:
    TICKETS_TRANSACTION = {
        "open": ["answered", "closed"],
        "answered": ["waiting_for_answer", "closed"],
        "waiting_for_answer": ["answered", "closed"],
    }

    @staticmethod
    def get_ticket_by_id(db: Session, id: UUID) -> Tickets:
        tickets_repo = TicketsRepository(db)
        existing_ticket = tickets_repo.find_one_or_none(id=id)
        if not existing_ticket:
            raise NotFound("Incorrect ticket id")
        return existing_ticket

    @staticmethod
    def create_new_ticket(
        db: Session, topic_name: str, text: str, email: str
    ) -> Tickets:
        current_date = datetime.now(tz=UTC)
        tickets_repo = TicketsRepository(db)
        status = "open"

        created_ticket = tickets_repo.insert_data(
            creation_date=current_date,
            modification_date=current_date,
            topic_name=topic_name,
            text=text,
            email=email,
            status=status,
        )
        return created_ticket

    def change_ticket_status(
        self, db: Session, id: UUID, status: TicketsStatus
    ) -> Tickets:
        current_date = datetime.now(tz=UTC)
        tickets_repo = TicketsRepository(db)

        existing_ticket = tickets_repo.find_one_or_none(id=id)
        if not existing_ticket:
            raise NotFound("Incorrect ticket id")

        allowed_statuses = self.TICKETS_TRANSACTION.get(existing_ticket.status.value)
        if not allowed_statuses or status.value not in allowed_statuses:
            raise BadRequest("Incorrect ticket status")

        updated_ticket = tickets_repo.update_fields_by_id(
            entity_id=existing_ticket.id, modification_date=current_date, status=status
        )
        return updated_ticket
