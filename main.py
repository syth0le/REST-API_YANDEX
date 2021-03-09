from flask import Flask, request

app = Flask('Candy Delivery App')


@app.route('/')
def index():
    return 'IT WORKS'


@app.route('/couriers', methods=['POST'])
def couriers():
    pass


@app.route('/couriers/<int:courier_id>', methods=['GET', 'PATCH'])
def courier_by_id():
    if request.method == 'GET':
        pass
    else:
        pass


@app.route('/orders', methods=['POST'])
def orders():
    pass


@app.route('/orders/assign', methods=['POST'])
def orders_assign():
    pass


@app.route('/orders/complete', methods=['POST'])
def orders_complete():
    pass


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)