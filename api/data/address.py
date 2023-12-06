class Address:
    def __init__(self, id_, flat, building, city, street, is_archieve, creator_id):
        self.id_ = id_
        self.flat = flat
        self.building = building
        self.city = city
        self.street = street
        self.is_archieve = is_archieve
        self.creator_id = creator_id


def create_address(flat, building, city, street, is_archieve, creator_id):
    params = ["flat", "building", "city", "street", "is_archieve", "creator_id"]

    args = [
        flat,
        building,
        city,
        street,
        is_archieve,
        creator_id
    ]

    helper.insert("auth_user", params, args)

    return find_address_by_unique(city, street, building, flat)


def find_address_by_unique(city, street, building, flat):
    line = helper.get("address", ["flat", "building", "city", "street"], [flat, building, city, street])
    address = Address(
        line[0], line[1], line[2], line[3],
        line[4], line[5], line[6], line[7]
    )

    return address
