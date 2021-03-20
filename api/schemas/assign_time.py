from marshmallow import fields, validate, Schema
from marshmallow_sqlalchemy import ModelSchema

from api.models.orders import Orders
from api.utils.db_init import db


class AssignTime(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        fields = ['assign_time']
        sqla_session = db.session

    assign_time = fields.String(required=True)
