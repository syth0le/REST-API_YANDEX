from marshmallow_sqlalchemy import ModelSchema
from api.models.couriers import *
from marshmallow import fields


class CouriersIds(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Couriers
        fields = ['id']
        sqla_session = db.session

    id = fields.Integer(required=True)