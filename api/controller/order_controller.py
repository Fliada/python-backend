import json

from fastapi import APIRouter

from api.data import order
from api.model.Order import OrderCreate, OrderUpdate
from api import JSONHelper

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


@order_routes.get('/all')
def get_orders():
    print("Orders")
    all_requests = order.get_all_requests()
    json_data = order.toJSON(all_requests)
    return json_data


@order_routes.get('/{order_id}')
def get_order(order_id: str):
    result_order = order.get_request(order_id)
    print('Возвращен заказ с номером %s' % order_id)
    return json.dumps(result_order)


# Оставить если нужно будет что-то поменять в заявке
@order_routes.put('/{order_id}')
def put_order(order_id: str):
    return 'Order %d' % order_id


@order_routes.put('/update/{order_id}')
def update_order(order_id: str, orderUpdate: OrderUpdate):
    order.update_request(order_id, orderUpdate.status_id)
    if orderUpdate.user_id is not None:
        order.update_request(order_id, "user_id", orderUpdate.user_id)
    if orderUpdate.address_id is not None:
        order.update_request(order_id, "address_id", orderUpdate.address_id)
    if orderUpdate.comment is not None:
        order.update_request(order_id, "comment", orderUpdate.comment)
    if orderUpdate.date_selected is not None:
        order.update_request(order_id, "date_selected", orderUpdate.date_selected)
    return 'Заказ %d был изменен' % order_id


# При повторе заявки дата тоже должна повторяться?
@order_routes.post('/repeat/{order_id}')
def repeat_order(order_id: str):
    new_order = order.find_request_by_id(order_id)
    order.create_request(new_order.user_id, new_order.address_id, new_order.comment, new_order.date_selected)
    return 'Repeat order %s' % order_id


@order_routes.delete('/{order_id}')
def delete_order(order_id: str):
    order.delete_request(order_id)

