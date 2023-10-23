from marshmallow import Schema, fields


class CommentsSchema(Schema):
    ticket_id = fields.UUID()
    author_email = fields.Email()
    text = fields.String()


class CommentsResponseSchema(CommentsSchema):
    id = fields.UUID()
    creation_date = fields.DateTime()
