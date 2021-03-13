from flask import Flask
from api.routes.couriers_route import couriers_page
from api.routes.orders_route import orders_page

app = Flask('Candy Delivery App')

app.register_blueprint(couriers_page, url_prefix='/couriers')
app.register_blueprint(orders_page, url_prefix='/orders')


@app.route('/')
def index():
    return 'IT WORKS'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
