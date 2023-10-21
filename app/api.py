from uuid import UUID

from flask import Blueprint, Response, request

from app.db import db_session
from app.schemas.comments import CommentsResponseSchema, CommentsSchema
from app.schemas.tickets import (
    TicketsResponseSchema,
    TicketsSchema,
    TicketsStatusChangeSchema,
)
from app.services.comments import CommentsService
from app.services.tickets import TicketsService
from app.utils.schemas import SIdUUID

tickets_router = Blueprint(
    name="tickets_router", import_name=__name__, url_prefix="/tickets"
)


@tickets_router.get("/<path:ticket_id>")
def get_ticket_by_id(ticket_id: UUID) -> [Response, int]:
    db = db_session()
    ticket_id = SIdUUID().load({"id": ticket_id})
    existing_ticket = TicketsService().get_ticket_by_id(db, **ticket_id)
    return TicketsResponseSchema().dump(existing_ticket), 200


@tickets_router.post("/")
def create_new_ticket() -> [Response, int]:
    db = db_session()
    data = request.get_json()
    new_ticket = TicketsSchema().load(data)
    created_ticket = TicketsService().create_new_ticket(db=db, **new_ticket)
    return TicketsResponseSchema().dump(created_ticket), 201


@tickets_router.patch("/<path:ticket_id>")
def change_ticket_status(ticket_id: UUID) -> [Response, int]:
    db = db_session()
    data = request.get_json()
    data.update({"id": ticket_id})

    new_status = TicketsStatusChangeSchema().load(data)
    updated_ticket = TicketsService().change_ticket_status(db=db, **new_status)
    return TicketsResponseSchema().dump(updated_ticket), 200


@tickets_router.post("/<path:ticket_id>/comments")
def create_new_comment(ticket_id: UUID) -> [Response, int]:
    db = db_session()
    data = request.get_json()
    data.update({"ticket_id": ticket_id})

    new_comment = CommentsSchema().load(data)
    created_comment = CommentsService().create_new_comment(db, **new_comment)
    return CommentsResponseSchema().dump(created_comment), 201
