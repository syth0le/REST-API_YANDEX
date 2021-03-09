from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from .courier_item import CourierItem, db, RegionsSchema, WorkingHours


class CourierUpdateRequest(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = CourierItem
        sqla_session = db.session

    courier_type = fields.String(required=True)
    regions = fields.Nested(RegionsSchema, many=True, only=['id', 'courier_id', 'region'])
    working_hours = fields.Nested(WorkingHours, many=True, only=['id', 'courier_id', 'hour'])
