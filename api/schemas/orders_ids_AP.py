from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrdersIdsAP(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        fields = ['id']
        sqla_session = db.session

    id = fields.Integer(required=True, dump_only=True)
