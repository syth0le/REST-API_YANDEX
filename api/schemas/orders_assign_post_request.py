from marshmallow import fields, Schema
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrdersAssignPostRequest(Schema):
    # class Meta(ModelSchema.Meta):
    #     model = OrdersInWork
    #     sqla_session = db.session

    courier_id = fields.Integer(required=True)
