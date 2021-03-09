from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Orders (object):
    __tablename__ = 'orders'

    order_id = db.Column(db.Integer())
    weight = db.Column(db.Numeric())
    region = db.Column(db.Integer())
    delivery_hours = db.relationship("DeliveryHours", backref="recipe", cascade="all, delete-orphan")
    # courier_id кому дали заказ


class DeliveryHours(object):
    id = db.Column(db.Integer())
    order_id = db.Column(db.Integer, db.ForeignKey('orders.orders_id'))
    hour = db.Column(db.String())
