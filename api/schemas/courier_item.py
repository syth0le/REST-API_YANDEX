from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models.couriers import *


class RegionsSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Regions
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    courier_id = fields.Integer(dump_only=True)
    region = fields.String(required=True)


class HoursSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = WorkingHours
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    courier_id = fields.Integer(dump_only=True)
    hour = fields.String(required=True)


class CourierItem(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Couriers
        sqla_session = db.session

    courier_id = fields.Number(dump_only=True)
    courier_type = fields.String(required=True)
    regions = fields.Nested(RegionsSchema, many=True, only=['id', 'courier_id', 'region'])
    working_hours = fields.Nested(WorkingHours, many=True, only=['id', 'courier_id', 'hour'])
