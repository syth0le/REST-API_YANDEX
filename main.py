import os
from flask import Flask
from api.routes.couriers_route import couriers_page
from api.routes.orders_route import orders_page
from api.utils.db_init import create_db

app = Flask('Candy Delivery App')
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'task.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

create_db(app)

app.register_blueprint(couriers_page, url_prefix='/couriers')
app.register_blueprint(orders_page, url_prefix='/orders')


@app.route('/')
def index():
    return 'IT WORKS'
