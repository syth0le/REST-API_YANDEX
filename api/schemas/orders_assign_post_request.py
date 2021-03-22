from marshmallow import fields, Schema
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrdersAssignPostRequest(Schema):

    courier_id = fields.Integer(required=True)
