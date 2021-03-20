from marshmallow import fields, Schema
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrdersIds(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        fields = ['id']
        sqla_session = db.session

    id = fields.Integer(required=True, dump_only=True)  # list of #  required orders -> ids
#  required orders