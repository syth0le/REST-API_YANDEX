from marshmallow import validate, fields
from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import ModelSchema

from api.models.couriers import *


class CourierItem(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Couriers
        fields = ["courier_id", "courier_type", "regions", "working_hours"]
        sqla_session = db.session

    courier_id = fields.Integer(required=True)
    # courier_type = EnumField(CourierType, by_value=True)
    courier_type = fields.String(required=True, validate=validate.OneOf(['foot', 'bike', 'car']))
    working_hours = fields.List(fields.String(validate=validate.Regexp(
            r"^(([01][0-9]|2[0-3]):[0-5][0-9]-([01][0-9]|2[0-3]):[0-5][0-9])$")),
            required=True,
            validate=validate.Length(min=1))
    regions = fields.List(fields.Integer(
        validate=[validate.Range(min=1), lambda x: isinstance(x, int)]),
        required=True,
        validate=validate.Length(min=1))
