from marshmallow import fields, validate, Schema
from marshmallow_sqlalchemy import ModelSchema
from api.models.couriers import *


class CourierGetResponse(Schema):
    # class Meta(ModelSchema.Meta):
    #     model = Couriers
    #     sqla_session = db.session

    courier_id = fields.Number(required=True)
    courier_type = fields.String(required=True)
    # regions = fields.Nested(Regions, many=True, only=['id', 'courier_id', 'region'])
    # working_hours = fields.Nested(WorkingHours, many=True, only=['id', 'courier_id', 'hour'])
    working_hours = fields.List(fields.String(), required=True, validate=validate.Length(min=1))
    regions = fields.List(fields.Integer(), required=True, validate=validate.Length(min=1))
    rating = fields.Number(required=True)  # Его нет в новой версии ответа
    earnings = fields.Integer(required=True)
