from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from api.models.couriers import *


class CourierUpdateRequest(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Couriers
        sqla_session = db.session

    courier_type = fields.String(required=True)
    regions = fields.Nested(Regions, many=True, only=['id', 'courier_id', 'region'])
    working_hours = fields.Nested(WorkingHours, many=True, only=['id', 'courier_id', 'hour'])
