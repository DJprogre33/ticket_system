from marshmallow import Schema, fields


class SIdUUID(Schema):
    id = fields.UUID()
