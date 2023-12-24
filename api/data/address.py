from dataclasses import dataclass

from api.db.DBHelper import DBHelper

helper = DBHelper()


@dataclass
class Address:
    id_: int
    flat: int
    building: int
    city: str
    street: str
    is_archieve: bool
    creator_id: int

    def __init__(self, id_, flat, building, city, street, is_archieve, creator_id):
        self.id_ = id_
        self.flat = flat
        self.building = building
        self.city = city
        self.street = street
        self.is_archieve = is_archieve
        self.creator_id = creator_id

    def set_archieve(self, is_archieve):
        self.is_archieve = is_archieve


def create_address(flat, building, city, street, creator_id):
    params = ["flat", "building", "city", "street", "is_archieve", "creator_id"]

    args = [
        flat,
        building,
        city,
        street,
        False,
        creator_id
    ]

    helper.insert("address", params, args)

    return find_address_by_unique(city, street, building, flat)


def find_address_by_unique(city, street, building, flat):
    line = helper.get("address", ["flat", "building", "city", "street"], [flat, building, city, street])[0]
    print(*line)
    address = Address(*line)

    return address

def find_address_by_id(_id):
    line = helper.get("address", ["id"], [_id])[0]
    addr = Address(*line)

    return addr

def get_all_addresses():
    lines = helper.print_info("address")

    addresses = []

    for l in lines:
        addresses.append(
            Address(*l)
        )

    return addresses


def get_all_addresses_by_id(_id):
    lines = helper.get("address", ["creator_id"], [_id])

    addresses = []

    for l in lines:
        if l[6] == _id:
            addresses.append(
                Address(*l)
            )

    return addresses


def get_archive_addresses_by_id(_id):
    lines = helper.get("address", ["creator_id"], [_id])

    addresses = []

    for l in lines:
        if l[6] == _id and l[5] == 'True':
            addresses.append(
                Address(*l)
            )

    return addresses


def update_address(_id, item, name):
    line = helper.update("address", "id", _id,  column_change=item, change=name)
    print(line)
    return line


def delete_address(id_):
    helper.delete("request", "creator_id", id_)
