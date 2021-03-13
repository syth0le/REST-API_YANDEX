from flask import request, Blueprint, jsonify
# from api.models.couriers import *
# from api.schemas.courier_get_response import *

couriers_page = Blueprint('couriers', __name__)


@couriers_page.route('/', methods=['POST'])
def couriers():
    if request.method == "POST":
        return '/couriers POST'
    else:
        print("POST")


@couriers_page.route('/<int:courier_id>', methods=['GET', 'PATCH'])
def courier_by_id(courier_id):
    if request.method == 'GET':
        # current_courier = Couriers.query.get_or_404(courier_id)
        # courier_schema = CourierGetResponse()
        # json_recipe = courier_schema.dump(current_courier)
        # return jsonify(json_recipe)
        return f'/couriers/{courier_id} GET'
    else:
        # PATCH METHOD REALISE
        return '/couriers/<int:courier_id> PATCH'
