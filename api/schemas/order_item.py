from marshmallow import fields, validate
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrderItem(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        sqla_session = db.session

    order_id = fields.Integer(required=True)
    weight = fields.Number(required=True, validate=validate.Range(min=0.01, max=50))
    region = fields.Integer(required=True)
    delivery_hours = fields.List(fields.String(
        validate=validate.Regexp(r"^(([01][0-9]|2[0-3]):[0-5][0-9]-([01][0-9]|2[0-3]):[0-5][0-9])$")),
        required=True, validate=validate.Length(min=1))
