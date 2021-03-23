from marshmallow import fields, Schema


class CouriersIdsAP(Schema):
    id = fields.Integer(required=True)

    # @post_dump
    # def change(self, data, **kwargs):
    #     data['id'] = data['order_id']
    #     del data['order_id']
    #     return data
