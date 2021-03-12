from main import *
from flask import request


@app.route('/')
def index():
    return 'IT WORKS'


@app.route('/couriers', methods=['POST'])
def couriers():
    return '/couriers POST'


@app.route('/couriers/<int:courier_id>', methods=['GET', 'PATCH'])
def courier_by_id(courier_id):
    if request.method == 'GET':
        return f'/couriers/{courier_id} GET'
    else:
        return '/couriers/<int:courier_id> PATCH'


@app.route('/orders', methods=['POST'])
def orders():
    return '/orders POST'


@app.route('/orders/assign', methods=['POST'])
def orders_assign():
    return '/orders/assign POST'


@app.route('/orders/complete', methods=['POST'])
def orders_complete():
    return '/orders/complete POST'
