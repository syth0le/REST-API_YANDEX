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

# migrate = Migrate(app, db) в инициализацию вставить


@app.route('/')
def index():
    return 'IT WORKS'

# достаем айдишники именно так:
# some_ids = [1, 2, 3, 4]
# query = "SELECT * FROM my_table t WHERE t.id = ANY(:ids);"
# conn.execute(sqlalchemy.text(query), ids=some_ids)