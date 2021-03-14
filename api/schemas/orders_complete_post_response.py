from marshmallow import fields, Schema
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrdersCompletePostRequest(Schema):
    # class Meta(ModelSchema.Meta):
    #     model = Orders
    #     sqla_session = db.session

    order_id = fields.Integer(required=True)
