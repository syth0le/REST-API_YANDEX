from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CourierItem (object):
    __tablename__ = 'couriers'

    courier_id = db.Column(db.Integer())
    courier_type = db.Column(db.String())
    regions = db.relationship("Regions", backref="recipe", cascade="all, delete-orphan")
    working_hours = db.relationship("Hours", backref="recipe", cascade="all, delete-orphan")
    rating = db.Column(db.Numeric())
    earnings = db.Column(db.Integer())


class Regions(object):
    id = db.Column(db.Integer())
    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.courier_id'))
    region = db.Column(db.Integer())


class WorkingHours(object):
    id = db.Column(db.Integer())
    courier_id = db.Column(db.Integer, db.ForeignKey('couriers.courier_id'))
    hour = db.Column(db.String())