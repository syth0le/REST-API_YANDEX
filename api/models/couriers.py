from api.utils.db_init import db
from enum import Enum


class CourierType(Enum):
    foot = "foot"
    bike = "bike"
    car = 'car'


class Couriers (db.Model):
    __tablename__ = 'couriers'
    DATA = {"foot": (2, 10), "bike": (5, 15), "car": (9, 50)}

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    courier_id = db.Column(db.Integer, unique=True)
    courier_type = db.Column(db.Enum(CourierType))
    regions = db.relationship("Regions", backref="couriers", cascade="all, delete-orphan")
    working_hours = db.relationship("Hours", backref="couriers", cascade="all, delete-orphan")
    rating = db.Column(db.Numeric)
    earnings = db.Column(db.Integer)
    weight_max = db.Column(db.Numeric, default=lambda: set_weight())
    weight_current = db.Column(db.Numeric, default=0)
    completed_orders = db.Column(db.Integer)
    delivery_times = db.relationship("Regions", backref="couriers", cascade="all, delete-orphan")
#
    # @weight_max.setter
    def set_weight(self, value, DATA):
        self.weight_max = self.DATA[self.courier_type][1]

    @property
    def salary(self):
        self.earnings = self.completed_orders * 500 * self.DATA[self.courier_type][0]
        return self._salary

    @property
    def rating(self):
        t = min(td[1], td[2], ..., td[n])
        (60 * 60 - min(t, 60 * 60)) / (60 * 60) * 5


class DeliveryTime(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.courier_id'))
    region = db.Column(db.Integer)
    delivery_time = db.Column(db.Integer)


class Regions(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.courier_id'))
    region = db.Column(db.Integer)


class WorkingHours(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.courier_id'))
    hour = db.Column(db.String(50))
