from marshmallow import fields, Schema, validate
from marshmallow_sqlalchemy import ModelSchema
from api.models.couriers import *


class CourierUpdateRequest(Schema):
    # class Meta(ModelSchema.Meta):
    #     model = Couriers
    #     sqla_session = db.session

    courier_type = fields.String()
    # regions = fields.Nested(RegionsSchema, many=True, only=['region'])
    # working_hours = fields.Nested(HoursSchema, many=True, only=['hour'])
    working_hours = fields.List(fields.String(), validate=validate.Length(min=1))
    regions = fields.List(fields.Integer(), validate=validate.Length(min=1))
