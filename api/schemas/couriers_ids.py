from marshmallow_sqlalchemy import ModelSchema
from .courier_item import CourierItem, db
from marshmallow import fields


class CourierId(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = CourierItem
        sqla_session = db.session

    courier_id = fields.Number(dump_only=True)
