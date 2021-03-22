from marshmallow_sqlalchemy import ModelSchema, fields
from marshmallow import Schema, validate, fields
from api.models.couriers import *


class CourierItem(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Couriers
        sqla_session = db.session

    courier_id = fields.Integer(required=True)
    courier_type = fields.String(required=True)
    working_hours = fields.List(fields.String(), required=True, validate=validate.Length(min=1))
    regions = fields.List(fields.Integer(), required=True, validate=validate.Length(min=1))

