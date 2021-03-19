from marshmallow_sqlalchemy import ModelSchema, fields
from marshmallow import Schema, validate, fields
from api.models.couriers import *


# class RegionsSchema(Schema):
#     # class Meta(ModelSchema.Meta):
#     #     model = Regions
#     #     sqla_session = db.session
#
#     id = fields.Number(dump_only=True)
#     courier_id = fields.Integer(dump_only=True)
#     region = fields.Integer(required=True)


# class HoursSchema(Schema):
#     # class Meta(ModelSchema.Meta):
#     #     model = WorkingHours
#     #     sqla_session = db.session
#
#     id = fields.Number(dump_only=True)
#     courier_id = fields.Integer(dump_only=True)
#     hour = fields.String(required=True)


class CourierItem(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Couriers
        sqla_session = db.session

    courier_id = fields.Integer(required=True)
    courier_type = fields.String(required=True)
    # regions = fields.Nested(RegionsSchema, many=True, only=['region'])
    # working_hours = fields.Nested(HoursSchema, many=True, only=['hour'])
    working_hours = fields.List(fields.String(), required=True, validate=validate.Length(min=1))
    regions = fields.List(fields.Integer(), required=True, validate=validate.Length(min=1))

    def get_max_weight(self, obj):
        if obj.courier_type == "foot":
            return 10
        elif obj.courier_type == "bike":
            return 15
        else:
            return 50
