import json
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from api.data import order, request_materials
from api.model.Order import OrderCreate, OrderUpdate
from api import JSONHelper
from api.roles import ROLES
from api.controller.user_controller import get_current_user

from dataclasses import asdict
from starlette.responses import JSONResponse

order_routes = APIRouter()


# РАБОТАЕТ
@order_routes.post('')
def insert_order(
        orderRequest: OrderCreate,
        current_user: dict = Depends(get_current_user)
    ):

    user_id = current_user.get("sub")
    address = orderRequest.address
    comment = orderRequest.comment
    date_selected = orderRequest.date_selected

    order.create_request(user_id, address, comment, date_selected)
    order_id = order.find_request_by_unique(user_id).id_

    materials = orderRequest.forms
    for mat in materials:
        request_materials.create_request_material(order_id, mat.material_id, mat.count)

    return 'Заказ создан'


@order_routes.get('/all')
def get_all_orders(
    current_user: dict = Depends(get_current_user)
):

    if current_user.get(ROLES.STAFF.value) == "False":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can get all orders")

    all_requests = order.get_all_requests()
    print(all_requests)
    return JSONResponse(content=[asdict(req) for req in all_requests])


@order_routes.get('/{order_id}')
def get_order(
        order_id: str,
        current_user: dict = Depends(get_current_user)
):
    if current_user.get(ROLES.STAFF.value) == "False":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can get the order")

    try:
        result_order = order.get_request(order_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Заказа не существует')

    print('Возвращен заказ с номером %s' % order_id)
    return JSONResponse(content=asdict(result_order))


@order_routes.get('')
def get_my_orders(
    current_user: dict = Depends(get_current_user)
):
    user_id = current_user.get("sub")
    all_requests = order.get_user_request(user_id)
    return JSONResponse(content=[asdict(req) for req in all_requests])


# Оставить если нужно будет что-то поменять в заявке
@order_routes.put('/{order_id}')
def put_order(
        order_id: str,
        current_user: dict = Depends(get_current_user)
):
    return 'Order %s' % order_id


@order_routes.put('/update/{order_id}')
def update_order(
        order_id: str,
        orderUpdate: OrderUpdate,
        current_user: dict = Depends(get_current_user)
):
    if not current_user.get(ROLES.STAFF.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can update the order")

    if orderUpdate.address is not None:
        order.update_request(order_id, "address", orderUpdate.address)
    if orderUpdate.comment is not None:
        order.update_request(order_id, "comment", orderUpdate.comment)
    if orderUpdate.date_selected is not None:
        order.update_request(order_id, "date_selected", orderUpdate.date_selected)
    if orderUpdate.status_id is not None:
        order.update_request(order_id, "status_id", orderUpdate.status_id)

    return 'Заказ %s был изменен' % order_id


# При повторе заявки дата тоже должна повторяться?
@order_routes.post('/repeat/{order_id}')
def repeat_order(
        order_id: str,
        current_user: dict = Depends(get_current_user)
):

    try:
        new_order = order.get_request(order_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Заказа не существует')

    if current_user.get("sub") != new_order.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can't repeat someone else's order")

    order.create_request(new_order.user_id, new_order.address, new_order.comment,
                         datetime.strptime(new_order.date_selected, "%Y-%m-%d %H:%M:%S"))

    _id = order.find_request_by_unique(new_order.user_id).id_

    materials = request_materials.get_all_request_material(order_id)
    for mat in materials:
        request_materials.create_request_material(_id, mat.material_id, mat.count)

    return f'Repeat order {order_id}'


@order_routes.delete('/{order_id}')
def delete_order(
        order_id: str,
        current_user: dict = Depends(get_current_user)
):
    if not current_user.get(ROLES.STAFF.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can delete the order")

    order.delete_request(order_id)

    request_materials.delete_request_material(order_id)

