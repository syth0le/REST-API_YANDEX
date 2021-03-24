import flask
from flask import request, Blueprint, jsonify, make_response
# from api.models.couriers import *
# from api.schemas.courier_get_response import *
from marshmallow import ValidationError

from api.models.couriers import Couriers
from api.models.orders import Orders
from api.schemas.courier_get_response import CourierGetResponse
from api.schemas.courier_update_request import CourierUpdateRequest
from api.schemas.couriers_ids import CouriersIds
from api.schemas.couriers_ids_AP import CouriersIdsAP
from api.schemas.couriers_post_request import CouriersPostRequest
from api.schemas.courier_item import CourierItem
from api.utils.db_init import db
from api.utils.get_earnings import get_salary
from api.utils.get_rating import get_rating
from api.utils.get_weight import get_weight

couriers_page = Blueprint('couriers', __name__)


@couriers_page.route('/', methods=['POST'])
def couriers():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        json_data = request.get_json()
        ids = list()
        if not json_data:
            return make_response(jsonify({"validation_error": {}})), 400
        try:
            courier_schema = CouriersPostRequest()
            couriers = courier_schema.load(json_data)
            for courier in couriers["data"]:
                courier_schema.dump(courier.create())
                ids.append({"id": courier.courier_id})
        except ValidationError as err:
            ids_AP_schema = CouriersIdsAP(many=True, unknown='EXCLUDE')
            for elem in list(err.messages["data"].keys()):
                ids.append({"id": err.valid_data["data"][elem]["courier_id"]})

            json_ids = ids_AP_schema.load(ids)
            json_ids = ids_AP_schema.dump(json_ids)
            return make_response(jsonify({"validation_error": {"couriers": json_ids}}), 400)

        ids_AP_schema = CouriersIdsAP(many=True, unknown='EXCLUDE')
        json_ids = ids_AP_schema.load(ids)
        json_ids = ids_AP_schema.dump(json_ids)
        return make_response(jsonify({"couriers": json_ids}), 201)


@couriers_page.route('/<int:courier_id>', methods=['GET', 'PATCH'])
def courier_by_id(courier_id):
    if request.method == 'GET':
        ###
        set_properties_courier = Couriers.find_by_courier_id(int(courier_id))
        if not set_properties_courier:
            return "Bad Request!", 400

        if set_properties_courier.completed_orders > 0:

            set_properties_courier.rating = get_rating(set_properties_courier.courier_id)
            # if set_properties_courier.rating != 0:
            set_properties_courier.earnings = get_salary(set_properties_courier.courier_type,
                                                         set_properties_courier.completed_orders)

            db.session.add(set_properties_courier)
            db.session.commit()
            #### До сюда все в шему перенести)))

        current_courier = Couriers.find_by_courier_id(courier_id)
        courier_schema = CourierGetResponse()
        json_result = courier_schema.dump(current_courier)

        return jsonify(json_result), 200
    else:
        current_courier = Couriers.find_by_courier_id(int(courier_id))
        old_hours = current_courier.working_hours
        old_type = current_courier.courier_type

        data = request.get_json()
        courier_upd_schema = CourierUpdateRequest()
        try:
            courier_upd = courier_upd_schema.load(data, instance=current_courier, partial=True)
        except ValidationError as err:
            return "Bad Request", 400
        db.session.add(courier_upd)
        db.session.commit()

        updated_courier = Couriers.find_by_courier_id(int(courier_id))
        orders = Orders.query.filter(Orders.courier_id == courier_id,
                                     Orders.completed == 0,
                                     Orders.assigned == 1).order_by(Orders.weight).all()
        print(orders)
        old_weight = get_weight(old_type)
        updated_weight = get_weight(updated_courier.courier_type)
        current_weight = 0
        for order in orders:
            print(f"order {order.delivery_hours}")
            current_weight += order.weight

            if old_hours != updated_courier.working_hours:
                print(old_hours)
                print(updated_courier.working_hours)

                if not any(item in updated_courier.working_hours for item in order.delivery_hours):
                    order.courier_id = None
                    order.assign_time = None
                    order.assigned = 0
                    db.session.add(courier_upd)

            if old_weight > updated_weight:
                if current_weight > updated_weight:
                    order.courier_id = None
                    order.assign_time = None
                    order.assigned = 0
                    db.session.add(courier_upd)
                else:
                    # print(f'MWFJOWJF {current_weight}')
                    pass

        db.session.commit()
        courier_schema = CourierItem()
        json_result = courier_schema.dump(updated_courier)
        return jsonify(json_result), 200
