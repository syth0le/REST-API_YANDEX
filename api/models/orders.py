from api.utils.db_init import db


class Orders (object):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer())
    weight = db.Column(db.Numeric())
    region = db.Column(db.Integer())
    delivery_hours = db.relationship("DeliveryHours", backref="recipe", cascade="all, delete-orphan")
    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.courier_id'))


class DeliveryHours(object):
    id = db.Column(db.Integer())
    order_id = db.Column(db.Integer, db.ForeignKey('orders.orders_id'))
    hour = db.Column(db.String())
