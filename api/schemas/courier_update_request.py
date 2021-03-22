from marshmallow import fields, Schema, validate
from marshmallow_sqlalchemy import ModelSchema
from api.models.couriers import *


class CourierUpdateRequest(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Couriers
        sqla_session = db.session

    courier_type = fields.String()
    working_hours = fields.List(fields.String(), validate=validate.Length(min=1))
    regions = fields.List(fields.Integer(), validate=validate.Length(min=1))
