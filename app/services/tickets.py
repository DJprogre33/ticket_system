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

    def __init__(self, db: Session):
        self.tickets_repo = TicketsRepository(db)

    def get_ticket_by_id(self, id: UUID) -> Tickets:
        existing_ticket = self.tickets_repo.find_one_or_none(id=id)
        if not existing_ticket:
            raise NotFound("Incorrect ticket id")
        return existing_ticket

    def create_new_ticket(self, topic_name: str, text: str, email: str) -> Tickets:
        current_date = datetime.now(tz=UTC)
        status = "open"

        created_ticket = self.tickets_repo.insert_data(
            creation_date=current_date,
            modification_date=current_date,
            topic_name=topic_name,
            text=text,
            email=email,
            status=status,
        )
        self.tickets_repo.commit()
        return created_ticket

    def change_ticket_status(self, id: UUID, status: TicketsStatus) -> Tickets:
        current_date = datetime.now(tz=UTC)

        existing_ticket = self.tickets_repo.find_one_or_none(id=id)
        if not existing_ticket:
            raise NotFound("Incorrect ticket id")

        allowed_statuses = self.TICKETS_TRANSACTION.get(existing_ticket.status.value)
        if not allowed_statuses or status.value not in allowed_statuses:
            raise BadRequest("Incorrect ticket status")

        updated_ticket = self.tickets_repo.update_fields_by_id(
            entity_id=existing_ticket.id, modification_date=current_date, status=status
        )
        self.tickets_repo.commit()
        return updated_ticket
