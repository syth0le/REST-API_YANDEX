from marshmallow import fields, Schema
from api.schemas.orders_post_request import OrdersPostRequest


class OrdersSchema(Schema):
    data = fields.Nested(OrdersPostRequest, many=True, required=True)
