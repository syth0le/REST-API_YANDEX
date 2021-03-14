from marshmallow import fields, Schema
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrdersIds(Schema):
    # class Meta(ModelSchema.Meta):
    #     model = Orders
    #     sqla_session = db.session

    order_id = fields.Integer(required=True)  # list of #  required orders -> ids
#  required orders