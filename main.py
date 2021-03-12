from flask import Flask

app = Flask('Candy Delivery App')

from api.routes.couriers_route import *

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
