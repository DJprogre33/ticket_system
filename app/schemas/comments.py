from marshmallow import Schema, fields


class SComments(Schema):
    ticket_id = fields.UUID()
    author_email = fields.Email()
    text = fields.String()


class SCommentsResponse(SComments):
    id = fields.UUID()
    creation_date = fields.DateTime()
