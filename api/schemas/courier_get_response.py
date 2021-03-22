from marshmallow import fields, validate, Schema
from marshmallow_sqlalchemy import ModelSchema
from api.models.couriers import *


class CourierGetResponse(Schema):

    courier_id = fields.Integer(required=True)
    courier_type = fields.String(required=True)
    working_hours = fields.List(fields.String(), required=True, validate=validate.Length(min=1))
    regions = fields.List(fields.Integer(), required=True, validate=validate.Length(min=1))
    rating = fields.Number(required=True)
    earnings = fields.Integer(required=True)
