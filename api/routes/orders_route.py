from flask import Blueprint, request, make_response, jsonify
from marshmallow import ValidationError

from api.models.orders import Orders
from api.schemas.orders_assign_post_request import OrdersAssignPostRequest
from api.schemas.orders_complete_post_request import OrdersCompletePostRequest
from api.schemas.order_item import OrderItem
from api.schemas.orders_ids import OrdersIds

orders_page = Blueprint('orders', __name__)


@orders_page.route('/', methods=['POST'])
def orders():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        json_data = request.get_json()
        if not json_data:
            current_smt = Orders.query.get_or_404(1)
            ids_schema = OrdersIds()
            json_ids = ids_schema.dump(current_smt)
            return make_response(jsonify({"validation_error": json_ids})), 400
        try:
            orders_schema = OrderItem()
            order = orders_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 400

        result = orders_schema.dump(order.create())
        # if db_sess.query(Couriers).get(json_data['courier_id']) is not None:
        #     raise Exception
        current_smt = Orders.query.get_or_404(1)
        ids_schema = OrdersIds()
        json_ids = ids_schema.dump(current_smt)
        return make_response(jsonify({"orders": json_ids}), 201)


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
