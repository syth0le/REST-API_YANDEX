from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

from .orders_post_request import Orders, db


class OrdersAssignPostRequest(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        sqla_session = db.session

    courier_id = fields.Integer(dump_only=True)
