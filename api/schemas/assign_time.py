from marshmallow import fields, validate, Schema


class AssignTime(Schema):

    assign_time = fields.String(required=True)
