from api.utils.db_init import db


class Orders (db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, unique=True)
    weight = db.Column(db.Numeric)
    region = db.Column(db.Integer)
    delivery_hours = db.relationship("DeliveryHours", backref="order", cascade="all, delete-orphan")
    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.courier_id'))
    assign_time = db.Column(db.String(50), default=0)
    complete_time = db.Column(db.String(50), default=0)


class DeliveryHours(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    hour = db.Column(db.String(50))
