from api.utils.db_init import db


class Orders (db.Model):
    """Couriers database class.

    Defining db Columns for correct initialization in SQL

    """
    __tablename__ = 'orders'

    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, unique=True, nullable=False)
    weight = db.Column(db.Float, default=0.0)
    region = db.Column(db.Integer, default=0)
    delivery_hours = db.Column(db.PickleType, nullable=False)
    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.courier_id'), nullable=True)
    assign_time = db.Column(db.DateTime, nullable=True)
    complete_time = db.Column(db.DateTime, nullable=True)
    difference_time = db.Column(db.Float, nullable=True)
    assigned = db.Column(db.Boolean, default=False)
    completed = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"{self.order_id}, {self.weight}, {self.delivery_hours}, {self.region}"

    def __repr__(self):
        return f"{self.__class__.__name__} {self.order_id}"

    def create(self):
        # function for creating and committing new database entry
        # returns object
        db.session.add(self)
        db.session.commit()
        return self

    def save(self):
        # function for saving changes in database
        db.session.add(self)
        db.session.commit()

    def delete(self):
        # delete post in db
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_order_id(cls, order_id):
        # finds courier in db by courier_id
        return cls.query.filter_by(order_id=order_id).first()
