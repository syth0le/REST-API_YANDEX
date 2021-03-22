from marshmallow import fields, Schema


class OrdersCompletePostRequest(Schema):
    class Meta(Schema.Meta):
        fields = ["courier_id", "complete_time", "order_id"]

    courier_id = fields.Integer(required=True)
    order_id = fields.Integer(required=True)
    complete_time = fields.String(required=True)
