from marshmallow import fields, post_dump
from marshmallow_sqlalchemy import ModelSchema
from api.models.orders import *


class OrdersIds(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        fields = ['order_id']
        sqla_session = db.session

    id = fields.Integer(required=True, dump_only=True)

    @post_dump
    def change(self, data, **kwargs):
        data['id'] = data['order_id']
        del data['order_id']
        return data
