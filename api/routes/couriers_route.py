from flask import request, Blueprint

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
        return f'/couriers/{courier_id} GET'
    else:
        return '/couriers/<int:courier_id> PATCH'
