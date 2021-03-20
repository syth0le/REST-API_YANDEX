from api.utils.db_init import db
from enum import Enum


class CourierType(Enum):
    foot = "foot"
    bike = "bike"
    car = 'car'

    def __str__(self):
        return str(self.value)


def set_weight(courier_type):
    DATA = {"foot": (2, 10), "bike": (5, 15), "car": (9, 50)}
    weight_max = DATA[courier_type][1]
    return weight_max


class Couriers(db.Model):
    __tablename__ = 'couriers'
    DATA = {"foot": (2, 10), "bike": (5, 15), "car": (9, 50)}

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    courier_id = db.Column(db.Integer, unique=True, nullable=False)
    courier_type = db.Column(db.Enum(CourierType))
    # regions = db.relationship("Regions", backref="courier", cascade="all, delete-orphan")
    # working_hours = db.relationship("WorkingHours", backref="courier", cascade="all, delete-orphan")
    regions = db.Column(db.PickleType, nullable=False)
    working_hours = db.Column(db.PickleType, nullable=False)
    rating = db.Column(db.Numeric, default=0.0)
    earnings = db.Column(db.Integer, default=0)
    # weight_max = db.Column(db.Numeric, default=lambda: set_weight(courier_type))
    weight_current = db.Column(db.Integer, default=0)
    completed_orders = db.Column(db.Integer, default=0)

    # delivery_times = db.relationship("Regions", backref="courier", cascade="all, delete-orphan")

    def __str__(self):
        return str(self.courier_id)

    def __repr__(self):
        return f"{self.__class__.__name__} {self.courier_id}"

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, data):
        for key, item in data:
            setattr(self, key, item)
        # self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    @classmethod
    def find_by_courier_id(cls, courier_id):
        return cls.query.filter_by(courier_id=courier_id).first()

    #
    # @property
    # def salary(self):
    #     self.earnings = self.completed_orders * 500 * self.DATA[self.courier_type][0]
    #     return self._salary
    #
    # @property
    # def rating(self):
    #     t = min(td[1], td[2], ..., td[n])
    #     (60 * 60 - min(t, 60 * 60)) / (60 * 60) * 5


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
