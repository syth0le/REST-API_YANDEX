from api.utils.db_init import db


class OrdersInWork(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    courier_id = db.Column(db.Integer, unique=True, nullable=False)
    order_id = db.Column(db.Integer, unique=True, nullable=False)
    weight = db.Column(db.Numeric, default=0.0)
    region = db.Column(db.Integer, default=0)

