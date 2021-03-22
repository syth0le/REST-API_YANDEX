from marshmallow import fields, Schema


class CouriersIdsAP(Schema):
    courier_id = fields.Integer(required=True)
