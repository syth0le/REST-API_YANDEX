import json

import flask
from flask import request, Blueprint, jsonify, make_response
# from api.models.couriers import *
# from api.schemas.courier_get_response import *
from marshmallow import ValidationError

from api.models.couriers import Couriers
from api.schemas.courier_get_response import CourierGetResponse
from api.schemas.courier_update_request import CourierUpdateRequest
from api.schemas.couriers_ids import CourierId
from api.schemas.couriers_post_request import CouriersPostRequest
from api.schemas.courier_item import CourierItem

couriers_page = Blueprint('couriers', __name__)


@couriers_page.route('/', methods=['POST'])
def couriers():
    if request.method == 'POST' and request.headers['Content-Type'] == 'application/json':
        json_data = request.get_json()
        if not json_data:
            current_smt = Couriers.query.get_or_404(1)
            ids_schema = CourierId()
            json_ids = ids_schema.dump(current_smt)
            return make_response(jsonify({"validation_error": json_ids})), 400
        try:
            courier_schema = CourierItem()
            courier = courier_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 400

        result = courier_schema.dump(courier.create())
        # if db_sess.query(Couriers).get(json_data['courier_id']) is not None:
        #     raise Exception
        current_smt = Couriers.query.get_or_404(1)
        ids_schema = CourierId()
        json_ids = ids_schema.dump(current_smt)
        status_code = flask.Response(status=201)
        return make_response(jsonify({"couriers": json_ids}), 201)

    # first, last = data["author"]["first"], data["author"]["last"]
    # author = Author.query.filter_by(first=first, last=last).first()
    # if author is None:
    #     # Create a new author
    #     author = Сouriers(first=first, last=last)
    #     db.session.add(author)
    #     # Create new quote
    # quote = Quote(
    #     content=data["content"], author=author, posted_at=datetime.datetime.utcnow()
    # )
    # db.session.add(quote)
    # db.session.commit()
    # result = quote_schema.dump(Quote.query.get(quote.id))


@couriers_page.route('/<int:courier_id>', methods=['GET', 'PATCH'])
def courier_by_id(courier_id):
    if request.method == 'GET':
        current_courier = Couriers.find_by_courier_id(courier_id)
        courier_schema = CourierGetResponse()
        json_recipe = courier_schema.dump(current_courier)
        return jsonify(json_recipe), 200
    else:
        current_courier = Couriers.query.get_or_404(courier_id)
        data = request.get_json()
        courier_schema = CourierUpdateRequest()
        courier_upd = courier_schema.load(data)
        return current_courier, 200
