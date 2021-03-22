from marshmallow import fields, Schema


class OrdersCompletePostRequest(Schema):

    courier_id = fields.Integer(required=True)
    order_id = fields.Integer(required=True)
    complete_time = fields.String(required=True)
