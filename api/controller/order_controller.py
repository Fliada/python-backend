from flask import Blueprint, session, request
from api.data import request
from api.data.request import get_all_requests, convert_requests_to_json, create_request

order_routes = Blueprint('order_routes', __name__)


@order_routes.route('/order/create', methods=['POST'])
def insert_order():
    if session['role'] == 'admin':
        data = request.get_json()

        user_id = data.get('user_id')
        staff_id = data.get('staff_id')
        address_id = data.get('address_id')
        comment = data.get('comment')
        status_id = data.get('status_id')
        date_creation = data.get('date_creation')
        date_selected = data.get('date_selected')
        date_actual = data.get('date_actual')
        create_request(user_id, staff_id, address_id, comment, status_id, date_creation, date_selected, date_actual)
        return 'Заказ создан'
    else:
        return "Недостаточно прав"


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order_routes.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return 'Order %d' % order_id


@order_routes.route('/orders', methods=['GET'])
def get_orders():
    print("Orders")
    all_requests = get_all_requests()
    json_data = convert_requests_to_json(all_requests)
    return json_data


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order_routes.route('/order/<int:post_id>', methods=['PUT'])
def put_order(order_id):
    return 'Order %d' % order_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order_routes.route('/order/repeat/<int:post_id>', methods=['POST'])
def repeat_order(order_id):
    return 'Repeat order %d' % order_id


@order_routes.route('/order/<int:post_id>', methods=['DELETE'])
def delete_order(order_id):
    if session['role'] == 'admin':
        request.delete_request(order_id)
        return 'Удалена заявка с Id %d' % order_id
    else:
        return "Недостаточно прав"

