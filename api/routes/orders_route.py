import datetime
import re
import sqlite3

import iso8601
import rfc3339
from flask import Blueprint, request, make_response, jsonify
from marshmallow import ValidationError

from api.models.couriers import Couriers
from api.models.orders import Orders
from api.schemas.assign_time import AssignTime
from api.schemas.couriers_post_request import CouriersPostRequest
from api.schemas.orders_assign_post_request import OrdersAssignPostRequest
from api.schemas.orders_complete_post_request import OrdersCompletePostRequest
from api.schemas.order_item import OrderItem
from api.schemas.orders_complete_post_response import OrdersCompletePostResponse
from api.schemas.orders_ids import OrdersIds
from api.schemas.orders_ids_AP import OrdersIdsAP
from api.schemas.orders_post_request import OrdersPostRequest
from api.utils.db_init import db
from api.utils.get_weight import get_weight

orders_page = Blueprint('orders', __name__)


@orders_page.route('/', methods=['POST'])
def orders_post():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        json_data = request.get_json()
        ids = list()
        if not json_data:
            return make_response(jsonify({"validation_error": {}})), 400
        try:
            orders_schema = OrdersPostRequest()
            orders = orders_schema.load(json_data)
            for order in orders["data"]:
                orders_schema.dump(order.create())
                ids.append({"id": order.order_id})
        except ValidationError as err:
            # print(err.valid_data["data"])
            ids_AP_schema = OrdersIdsAP(many=True, unknown='EXCLUDE')
            for elem in list(err.messages["data"].keys()):
                ids.append({"id": err.valid_data["data"][elem]["order_id"]})

            json_ids = ids_AP_schema.load(ids)
            json_ids = ids_AP_schema.dump(json_ids)
            return make_response(jsonify({"validation_error": {"orders": json_ids}}), 400)

        ids_AP_schema = OrdersIdsAP(many=True, unknown='EXCLUDE')
        json_ids = ids_AP_schema.load(ids)
        json_ids = ids_AP_schema.dump(json_ids)
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
            max_courier_weight = get_weight(courier.courier_type)
        except:
            return "Bad Request", 400
        orders_assigned_ids_schema = OrdersIds(many=True)
        assign_time = datetime.datetime.utcnow()
        current_weight = 0
        if len(courier.regions) > 1:
            sql = f"select * from Orders where region in {tuple(courier.regions)} AND assigned == False AND completed == False order by weight"
        else:
            sql = f"select * from Orders where region == {courier.regions[0]} AND assigned == False AND completed == False order by weight"

        result = db.session.execute(sql)

        for elem in result:
            order_weight = elem.weight

            if courier.weight_current + order_weight > max_courier_weight:
                return make_response(jsonify({"orders": []}), 200)

            if current_weight + order_weight > max_courier_weight:
                break

            current_smt = Orders.query.get(elem.id)
            if any(item in current_smt.delivery_hours for item in courier.working_hours):
                current_smt.assign_time = assign_time
                current_smt.courier_id = courier.courier_id
                current_smt.assigned = True
                db.session.add(current_smt)

                current_weight += order_weight

        courier.weight_current += current_weight
        db.session.add(courier)
        db.session.commit()

        orders_assigned_ids = Orders.query.filter(Orders.courier_id == courier_id, Orders.completed == 0).all()
        if not orders_assigned_ids:
            return make_response(jsonify({"orders": []}), 200)
        # print(orders_assigned_ids)
        time_schema = AssignTime(many=True)
        result_time = time_schema.dump(orders_assigned_ids)
        json_result = orders_assigned_ids_schema.dump(orders_assigned_ids)
        # print(json_result)
        return make_response(jsonify({"orders": json_result, "assign_time": result_time[0]}), 200)


@orders_page.route('/complete', methods=['POST'])
def orders_complete():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        order_complete_schema_request = OrdersCompletePostRequest()
        order_complete = order_complete_schema_request.load(data)
        courier_id = order_complete['courier_id']
        order_id = order_complete['order_id']
        complete_time = iso8601.parse_date(order_complete['complete_time']).replace(tzinfo=None)
        # В случае, если заказ не найден, был назначен на другого курьера или не назначен вовсе,
        # следует вернуть ошибку HTTP 400 Bad Request 

        current_courier = Couriers.find_by_courier_id(int(courier_id))
        orders_to_complete = Orders.query.filter(Orders.courier_id == courier_id, Orders.order_id == order_id).first()

        if orders_to_complete is None or not orders_to_complete.assigned:
            return "Bad Request", 400
        if orders_to_complete.completed:
            return make_response(jsonify({"orders_id": orders_to_complete.order_id}), 200)

        orders_to_complete.completed = True
        orders_to_complete.complete_time = complete_time
        orders_to_complete.difference_time = (complete_time-orders_to_complete.assign_time).total_seconds()
        current_courier.weight_current -= orders_to_complete.weight
        current_courier.completed_orders += 1

        db.session.add(orders_to_complete)
        db.session.add(current_courier)
        db.session.commit()

        pre_complete_time(courier_id, complete_time)
        order_to_complete = Orders.query.filter(Orders.order_id == order_id).first()
        order_complete_schema_response = OrdersCompletePostResponse()
        json_result = order_complete_schema_response.dump(order_to_complete)
        return make_response(jsonify(json_result), 200)


def pre_complete_time(courier_id, complete_time):
    orders_retime = Orders.query.filter(Orders.courier_id == courier_id, Orders.completed == 0).all()
    for order in orders_retime:
        order.assign_time = complete_time
        db.session.add(order)
        db.session.commit()
