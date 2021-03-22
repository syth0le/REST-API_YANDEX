from marshmallow import fields, Schema
from api.schemas.courier_item import CourierItem


class CouriersPostRequest(Schema):
    class Meta(Schema.Meta):
        fields = ['data']

    data = fields.Nested(CourierItem, many=True, required=True)
