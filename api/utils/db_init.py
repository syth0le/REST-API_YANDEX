from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_db(app):
    from api.models.couriers import Couriers
    from api.models.orders import Orders

    db.init_app(app)

    with app.app_context():
        db.create_all()
