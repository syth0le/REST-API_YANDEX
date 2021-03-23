from marshmallow import fields, validate, Schema, pre_dump, post_dump
from marshmallow_enum import EnumField

from api.models.couriers import *


class CourierGetResponse(Schema):

    courier_id = fields.Integer(required=True)
    # courier_type = EnumField(CourierType, by_value=True)
    courier_type = fields.String(required=True, validate=validate.OneOf(['foot', 'bike', 'car']))
    working_hours = fields.List(fields.String(), required=True, validate=validate.Length(min=1))
    regions = fields.List(fields.Integer(), required=True, validate=validate.Length(min=1))
    rating = fields.Number()
    earnings = fields.Integer(required=True)

    @post_dump
    def get_rating(self, out_data, **kwargs):
        if out_data['rating'] is None:
            del out_data['rating']
        else:
            pass
        return out_data
