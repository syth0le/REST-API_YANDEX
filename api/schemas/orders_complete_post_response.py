from marshmallow import fields, Schema
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrdersCompletePostResponse(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        fields = ['order_id']
        sqla_session = db.session

    order_id = fields.Integer(required=True)

