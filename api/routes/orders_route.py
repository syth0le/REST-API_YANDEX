import datetime

from flask import Blueprint, request, make_response, jsonify
from marshmallow import ValidationError

from api.models.couriers import Couriers
from api.models.orders import Orders
from api.schemas.orders_assign_post_request import OrdersAssignPostRequest
from api.schemas.orders_complete_post_request import OrdersCompletePostRequest
from api.schemas.order_item import OrderItem
from api.schemas.orders_ids import OrdersIds
from api.utils.db_init import db

orders_page = Blueprint('orders', __name__)


def get_weight(courier_type):
    DATA = {"foot": (2, 10), "bike": (5, 15), "car": (9, 50)}
    weight_max = DATA[str(courier_type)][1]
    return weight_max


@orders_page.route('/', methods=['POST'])
def orders_post():
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
        assign_to_courier = orders_assign_schema.load(data)
        courier_id = assign_to_courier['courier_id']
        try:
            courier = Couriers.find_by_courier_id(courier_id)
        except:
            return "BAD REQUEST", 400
        max_courier_weight = get_weight(courier.courier_type)
        orders_assigned_ids_schema = OrdersIds(many=True)
        assign_time = datetime.datetime.utcnow()
        current_weight = 0
        # print(courier.regions)

        sql = f"select * from Orders where region in {tuple(courier.regions)} AND assigned == False AND completed == False order by weight"
        result = db.engine.execute(sql)

        for elem in result:
            # print(elem)
            order_weight = elem.weight

            if courier.weight_current + order_weight > max_courier_weight:
                print("BREAK= нельзя дать заказ у курьера дозуя заказов")
                return make_response(jsonify({"orders": []}), 200)

            if current_weight + order_weight > max_courier_weight:
                print("BREAK=" + str(current_weight + order_weight))
                break

            current_smt = Orders.query.get(elem.id)
            current_smt.assign_time = assign_time
            current_smt.courier_id = courier.courier_id
            current_smt.assigned = True
            db.session.add(current_smt)

            current_weight += order_weight
            print(f"current weight = {current_weight}")

        print(f"final weight = {current_weight}")

        courier.weight_current += current_weight
        db.session.add(courier)
        db.session.commit()

        result_time = str(assign_time.isoformat())

        orders_assigned_ids = Orders.query.filter(Orders.courier_id == courier_id, Orders.completed == 0).all()
        print(orders_assigned_ids)
        json_result = orders_assigned_ids_schema.dump(orders_assigned_ids)
        return make_response(jsonify({"orders": json_result, "assign_time": result_time}), 200)


@orders_page.route('/complete', methods=['POST'])
def orders_complete():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        orders_complete_schema = OrdersCompletePostRequest()
        orders = orders_complete_schema.load(data)
        # result = courier_schema.dump(courier.create())
        return orders
