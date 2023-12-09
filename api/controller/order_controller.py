from fastapi import APIRouter

from api.data import order
from api.data.order import get_all_requests, convert_requests_to_json, create_request
from api.model.Order import OrderCreate

order_routes = APIRouter()


# РАБОТАЕТ
@order_routes.post('/create')
def insert_order(orderRequest: OrderCreate):

    user_id = orderRequest.user_id
    address_id = orderRequest.address_id
    comment = orderRequest.comment
    date_selected = orderRequest.date_selected
    create_request(user_id, address_id, comment, date_selected)
    return 'Заказ создан'


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order_routes.get('/<int:order_id>')
def get_order(order_id):
    return 'Order %d' % order_id


@order_routes.get('/all')
def get_orders():
    print("Orders")
    all_requests = get_all_requests()
    json_data = convert_requests_to_json(all_requests)
    return json_data


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order_routes.put('/<int:order_id>')
def put_order(order_id):
    return 'Order %d' % order_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order_routes.post('/repeat/<int:order_id>')
def repeat_order(order_id):
    return 'Repeat order %d' % order_id


@order_routes.delete('/<int:order_id>')
def delete_order(order_id):
    order.delete_request(order_id)

