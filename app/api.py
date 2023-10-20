from uuid import UUID

from flask import Response, jsonify, request

from app.db import db_session
from app.main import app
from app.schemas.comments import SComments, SCommentsResponse
from app.schemas.tickets import STickets, STicketsResponse, STicketsStatusChange
from app.services.comments import CommentsService
from app.services.tickets import TicketsService
from app.utils.schemas import SIdUUID


@app.get("/tickets/<path:ticket_id>")
def get_ticket_by_id(ticket_id: UUID) -> [Response, int]:
    db = db_session()
    ticket_id = SIdUUID().load({"id": ticket_id})
    existing_ticket = TicketsService().get_ticket_by_id(db, **ticket_id)
    return jsonify(STicketsResponse().dump(existing_ticket)), 200


@app.post("/tickets/new")
def create_new_ticket() -> [Response, int]:
    db = db_session()
    data = request.get_json()
    new_ticket = STickets().load(data)
    created_ticket = TicketsService().create_new_ticket(db=db, **new_ticket)
    return jsonify(STicketsResponse().dump(created_ticket)), 201


@app.patch("/tickets/<path:ticket_id>")
def change_ticket_status(ticket_id: UUID) -> [Response, int]:
    db = db_session()
    data = request.get_json()
    data.update({"id": ticket_id})

    new_status = STicketsStatusChange().load(data)
    updated_ticket = TicketsService().change_ticket_status(db=db, **new_status)
    return jsonify(STicketsResponse().dump(updated_ticket)), 200


@app.post("/tickets/<path:ticket_id>/comments/new")
def create_new_comment(ticket_id: UUID) -> [Response, int]:
    db = db_session()
    data = request.get_json()
    data.update({"ticket_id": ticket_id})

    new_comment = SComments().load(data)
    created_comment = CommentsService().create_new_comment(db, **new_comment)
    return jsonify(SCommentsResponse().dump(created_comment)), 201
