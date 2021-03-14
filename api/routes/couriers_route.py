from flask import request, Blueprint, jsonify
# from api.models.couriers import *
# from api.schemas.courier_get_response import *
from api.schemas.courier_update_request import CourierUpdateRequest
from api.schemas.couriers_post_request import CouriersPostRequest
from api.schemas.courier_item import CourierItem

couriers_page = Blueprint('couriers', __name__)


@couriers_page.route('/', methods=['POST'])
def couriers():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        # courier_schema = CouriersPostRequest()
        courier_schema = CouriersPostRequest()
        courier = courier_schema.load(data)
        # result = courier_schema.dump(courier.create())
        return courier


@couriers_page.route('/<int:courier_id>', methods=['GET', 'PATCH'])
def courier_by_id(courier_id):
    if request.method == 'GET':
        # current_courier = Couriers.query.get_or_404(courier_id)
        # courier_schema = CourierGetResponse()
        # json_recipe = courier_schema.dump(current_courier)
        # return jsonify(json_recipe)
        return f'/couriers/{courier_id} GET'
    else:
        # current_courier = Couriers.query.get_or_404(courier_id)
        data = request.get_json()
        courier_schema = CourierUpdateRequest()
        courier_upd = courier_schema.load(data)
        return courier_upd
