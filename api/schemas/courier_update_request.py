from marshmallow import fields, Schema, validate
from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import ModelSchema
from api.models.couriers import *


class CourierUpdateRequest(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Couriers
        fields = ["courier_type", "working_hours", "regions"]
        sqla_session = db.session

    # courier_type = EnumField(CourierType, by_value=True)
    courier_type = fields.String(required=True, validate=validate.OneOf(['foot', 'bike', 'car']))
    working_hours = fields.List(fields.String(), validate=validate.Length(min=1))
    regions = fields.List(fields.Integer(), validate=validate.Length(min=1))
