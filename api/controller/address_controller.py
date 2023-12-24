from dataclasses import asdict

from fastapi import APIRouter, Depends, HTTPException, status

from api.data import address
from api.model.Address import AddressCreate

from api.controller.user_controller import get_current_user
from starlette.responses import JSONResponse

from api.model.Address import AddressUpdate
from api.roles import ROLES

address_routes = APIRouter()


@address_routes.post('/create')
def insert_address(
        addressRequest: AddressCreate,
        current_user: dict = Depends(get_current_user)
):
    flat = addressRequest.flat
    building = addressRequest.building
    city = addressRequest.city
    street = addressRequest.street
    creator_id = addressRequest.creator_id
    address.create_address(flat, building, city, street, creator_id)
    return 'Адрес создан'


@address_routes.get('')
def get_user_addresses(
        current_user: dict = Depends(get_current_user)
):
    all_addresses = address.get_all_addresses_by_id(current_user.get("sub"))
    return JSONResponse(content=[asdict(addr) for addr in all_addresses])


@address_routes.get('/archive')
def get_user_archive_addresses(
        current_user: dict = Depends(get_current_user)
):
    all_addresses = address.get_archive_addresses_by_id(current_user.get("sub"))
    return JSONResponse(content=[asdict(addr) for addr in all_addresses])


@address_routes.put('/update/{address_id}')
def update_address(
        address_id: str,
        addressUpdate: AddressUpdate,
        current_user: dict = Depends(get_current_user)
):
    if not current_user.get(ROLES.STAFF.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can update the address")

    try:
        new_address = address.find_address_by_id(address_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Address does not exist')

    if current_user.get("sub") != new_address.creator_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can't repeat someone else's order")

    if addressUpdate.is_archieve is not None:
        address.update_address(address_id, "is_archieve", addressUpdate.is_archieve)

    return 'Заказ %s был изменен' % address_id


@address_routes.delete('/delete')
def delete_address(
        id_,
        current_user: dict = Depends(get_current_user)
):
    address.delete_address(id_)
