from marshmallow import fields, Schema


class OrdersIdsAP(Schema):
    order_id = fields.Integer(required=True)
