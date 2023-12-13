from flask import Blueprint, session, request
from api.data import order
from api.data.address import create_address
from api.data.material import create_material, delete_material

address_routes = Blueprint('address_routes', __name__)


@address_routes.route('/address/create', methods=['POST'])
def insert_address():
    data = request.get_json()

    #"id", "flat", "building", "city", "street", "is_archieve", "creator_id"

    flat = data.get('flat')
    building = data.get('building')
    city = data.get('city')
    street = data.get('street')
    creator_id = data.get('creator_id')
    create_address(flat, building, city, street, creator_id)
    return 'Адрес создан'
from fastapi import APIRouter

from api.data import address
from api.model.Address import AddressCreate

address_routes = APIRouter()


@address_routes.post('/create')
def insert_address(addressRequest: AddressCreate):
    flat = addressRequest.flat
    building = addressRequest.building
    city = addressRequest.city
    street = addressRequest.street
    creator_id = addressRequest.creator_id
    address.create_address(flat, building, city, street, creator_id)
    return 'Адрес создан'


@address_routes.delete('/delete')
def delete_address(city, street, building, flat):
    address.delete_address(city, street, building, flat)
