from marshmallow import fields, validate
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrderItem(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        sqla_session = db.session

    order_id = fields.Integer(required=True)
    weight = fields.Number(required=True)
    region = fields.Integer(required=True)
    delivery_hours = fields.List(fields.String(), required=True, validate=validate.Length(min=1))
