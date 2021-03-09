from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from .courier_item import CourierItem, db, RegionsSchema, WorkingHours


class CourierGetResponse(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = CourierItem
        sqla_session = db.session

    courier_id = fields.Number(dump_only=True)
    courier_type = fields.String(required=True)
    regions = fields.Nested(RegionsSchema, many=True, only=['id', 'courier_id', 'region'])
    working_hours = fields.Nested(WorkingHours, many=True, only=['id', 'courier_id', 'hour'])
    ratings = fields.Number(dump_only=True)
    earnings = fields.Integer(dump_only=True)