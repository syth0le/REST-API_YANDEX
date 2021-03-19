from marshmallow_sqlalchemy import ModelSchema
from api.models.couriers import *
from marshmallow import fields, Schema


class CourierId(Schema):
    # class Meta(ModelSchema.Meta):
    #     model = Couriers
    #     sqla_session = db.session

    id = fields.Integer(required=True)  # list of #  required couriers -> ids
#  required couriers