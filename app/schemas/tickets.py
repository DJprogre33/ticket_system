from marshmallow import Schema, fields

from app.models.tickets import TicketsStatus


class TicketsSchema(Schema):
    topic_name = fields.String()
    text = fields.String()
    email = fields.Email()


class TicketsResponseSchema(TicketsSchema):
    id = fields.UUID()
    created_date = fields.DateTime()
    updated_date = fields.DateTime()
    status = fields.Enum(TicketsStatus)


class TicketsStatusChangeSchema(Schema):
    id = fields.UUID()
    status = fields.Enum(TicketsStatus)
