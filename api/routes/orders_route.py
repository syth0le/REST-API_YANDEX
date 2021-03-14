from flask import Blueprint, request

from api.schemas.orders_assign_post_request import OrdersAssignPostRequest
from api.schemas.orders_complete_post_request import OrdersCompletePostRequest
from api.schemas.order_item import OrderItem

orders_page = Blueprint('orders', __name__)


@orders_page.route('/', methods=['POST'])
def orders():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        orders_schema = OrderItem()
        orders = orders_schema.load(data)
        # result = courier_schema.dump(courier.create())
        return orders


@orders_page.route('/assign', methods=['POST'])
def orders_assign():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        orders_assign_schema = OrdersAssignPostRequest()
        # orders_schema = OrdersPostRequest()
        orders = orders_assign_schema.load(data)
        # result = courier_schema.dump(courier.create())
        return orders


@orders_page.route('/complete', methods=['POST'])
def orders_complete():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        orders_complete_schema = OrdersCompletePostRequest()
        orders = orders_complete_schema.load(data)
        # result = courier_schema.dump(courier.create())
        return orders
