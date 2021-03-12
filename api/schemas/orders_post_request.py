from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrdersPostRequest(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        sqla_session = db.session

    order_id = fields.Integer(dump_only=True)
    weight = fields.Number(required=True)
    region = fields.Integer(required=True)
    delivery_hours = fields.Nested(DeliveryHours, many=True, only=['id', 'orders_id', 'hour'])
