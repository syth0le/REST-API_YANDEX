from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from api.models.couriers import *


class CourierGetResponse(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Couriers
        sqla_session = db.session

    courier_id = fields.Number(dump_only=True)
    courier_type = fields.String(required=True)
    regions = fields.Nested(Regions, many=True, only=['id', 'courier_id', 'region'])
    working_hours = fields.Nested(WorkingHours, many=True, only=['id', 'courier_id', 'hour'])
    rating = fields.Number(dump_only=True)
    earnings = fields.Integer(dump_only=True)
