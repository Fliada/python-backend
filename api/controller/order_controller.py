import json

from fastapi import APIRouter

from api.data import order
from api.model.Order import OrderCreate

order_routes = APIRouter()


# РАБОТАЕТ
@order_routes.post('/create')
def insert_order(orderRequest: OrderCreate):

    user_id = orderRequest.user_id
    address_id = orderRequest.address_id
    comment = orderRequest.comment
    date_selected = orderRequest.date_selected
    order.create_request(user_id, address_id, comment, date_selected)
    return 'Заказ создан'


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order_routes.get('/<int:order_id>')
def get_order(order_id):
    result_order = order.get_request(order_id)
    print('Возвращен заказ с номером %d' % order_id)
    return json.dumps(result_order)


@order_routes.get('/all')
def get_orders():
    print("Orders")
    all_requests = order.get_all_requests()
    json_data = order.convert_requests_to_json(all_requests)
    return json_data


# Оставить если нужно будет что-то поменять в заявке
@order_routes.put('/<int:order_id>')
def put_order(order_id):
    return 'Order %d' % order_id


# При повторе заявки дата тоже должна повторяться?
@order_routes.post('/repeat/<int:order_id>')
def repeat_order(order_id):
    new_order = order.find_request_by_id(order_id)
    order.create_request(new_order.user_id, new_order.address_id, new_order.comment, new_order.date_selected)
    return 'Repeat order %d' % order_id


@order_routes.delete('/<int:order_id>')
def delete_order(order_id):
    order.delete_request(order_id)

