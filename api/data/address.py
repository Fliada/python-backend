from api.db.DBHelper import DBHelper

helper = DBHelper()

class Address:
    def __init__(self, id_, flat, building, city, street, creator_id):
        self.id_ = id_
        self.flat = flat
        self.building = building
        self.city = city
        self.street = street
        self.is_archieve = None
        self.creator_id = creator_id

    def set_archieve(self, is_archieve):
        self.is_archieve = is_archieve


def create_address(flat, building, city, street, creator_id):
    params = ["flat", "building", "city", "street", "creator_id"]

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
    line = helper.get("address", ["flat", "building", "city", "street"], [flat, building, city, street])
    address = Address(
        line[0], line[1], line[2], line[3],
        line[4], line[5], line[6]
    )

    return address


def get_all_addresses():
    lines = helper.print_info("address")

    addresses = []

    for l in lines:
        addresses.append(
            Address(
                l[0], l[1], l[2], l[3],
                l[4], l[5], l[6]
            )
        )

    return addresses


def get_all_addresses_by_id(_id):
    lines = helper.get("address", ["flat", "building", "city", "street"], [flat, building, city, street])

    addresses = []

    for l in lines:
        if l[6] == _id:
            addresses.append(
                Address(
                    l[0], l[1], l[2], l[3],
                    l[4], l[5], l[6]
                )
            )

    return addresses


def get_archive_addresses_by_id(_id):
    lines = helper.get("address", ["flat", "building", "city", "street"], [flat, building, city, street])

    addresses = []

    for l in lines:
        if l[6] == _id and l[5] == 'TRUE':
            addresses.append(
                Address(
                    l[0], l[1], l[2], l[3],
                    l[4], l[5], l[6]
                )
            )

    return addresses


def delete_address(city, street, building, flat):
    helper.delete("request", ["flat", "building", "city", "street"], [city, street, building, flat])
