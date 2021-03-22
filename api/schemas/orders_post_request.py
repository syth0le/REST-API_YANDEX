from marshmallow import fields, Schema
from api.schemas.order_item import OrderItem


class OrdersPostRequest(Schema):
    data = fields.Nested(OrderItem, many=True, required=True)
