from marshmallow_sqlalchemy import ModelSchema
from api.models.couriers import *
from marshmallow import fields


class CourierId(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Couriers
        sqla_session = db.session

    courier_id = fields.Number(dump_only=True)
