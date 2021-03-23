from api.utils.courier_type import CourierType
from api.utils.db_init import db


def set_weight(courier_type):
    DATA = {"foot": (2, 10), "bike": (5, 15), "car": (9, 50)}
    weight_max = DATA[courier_type][1]
    return weight_max


class Couriers(db.Model):
    __tablename__ = 'couriers'
    DATA = {"foot": (2, 10), "bike": (5, 15), "car": (9, 50)}

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    courier_id = db.Column(db.Integer, unique=True, nullable=False)
    courier_type = db.Column(db.String(30))
    regions = db.Column(db.PickleType, nullable=False)
    working_hours = db.Column(db.PickleType, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    earnings = db.Column(db.Float, default=0.0)
    # weight_max = db.Column(db.Float, default=lambda: set_weight(courier_type))
    weight_current = db.Column(db.Float, default=0.0)
    completed_orders = db.Column(db.Integer, default=0)

    def __str__(self):
        return f"{self.courier_id}, {self.courier_type}, {self.working_hours}, {self.regions}"

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
