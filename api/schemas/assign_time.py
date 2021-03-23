from marshmallow import fields, validate, Schema, post_dump, pre_dump
from marshmallow_sqlalchemy import ModelSchema

from api.models.orders import Orders
from api.utils.db_init import db


class AssignTime(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Orders
        fields = ['assign_time']
        sqla_session = db.session

    assign_time = fields.String()

    @pre_dump
    def time_convertation(self, out_data, **kwargs):
        out_data.assign_time = out_data.assign_time.isoformat()
        return out_data
