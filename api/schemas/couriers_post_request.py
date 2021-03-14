from marshmallow import fields, Schema
from api.schemas.courier_item import CourierItem


class CouriersPostRequest(Schema):
    data = fields.Nested(CourierItem, many=True, required=True)
