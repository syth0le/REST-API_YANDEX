from marshmallow import fields, validate, Schema
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrdersPostRequest(Schema):
    # class Meta(ModelSchema.Meta):
    #     model = Orders
    #     sqla_session = db.session

    order_id = fields.Integer(required=True)
    weight = fields.Float(required=True)
    region = fields.Integer(required=True)
    # delivery_hours = fields.Nested(DeliveryHours, many=True, only=['id', 'orders_id', 'hour'])
    delivery_hours = fields.List(fields.String(), required=True, validate=validate.Length(min=1))
