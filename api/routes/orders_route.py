from flask import Blueprint

orders_page = Blueprint('orders', __name__)


@orders_page.route('/', methods=['POST'])
def orders():
    return '/orders POST'


@orders_page.route('/assign', methods=['POST'])
def orders_assign():
    return '/orders/assign POST'


@orders_page.route('/complete', methods=['POST'])
def orders_complete():
    return '/orders/complete POST'
