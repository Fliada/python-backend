from dataclasses import dataclass

from api.db.DBHelper import DBHelper

helper = DBHelper()


@dataclass
class Request_material:
    material_id: int
    material: str
    count: int
    units: str
    category: str

    def __init__(self, id_, material, count, units, category):
        self.material_id = id_
        self.material = material
        self.count = count
        self.units = units
        self.category = category


def create_request_material(request_id, material_id, count):
    params = ["request_id", "material_id", "count"]

    args = [
        request_id,
        material_id,
        count
    ]

    helper.insert("request_materials", params, args)


def get_all_request_material(order_id):
    req = f"SELECT m.id, m.name, rm.count, m.units, c.name " \
          f"FROM request_materials rm " \
          f"JOIN material m " \
          f"ON rm.material_id = m.id " \
          f"JOIN category c " \
          f"ON c.id = m.category_id " \
          f"WHERE rm.request_id = '{order_id}'"

    lines = helper.any_request(req)

    reqs = []

    for l in lines:
        reqs.append(
            Request_material(*l)
        )

    print(reqs)
    return reqs


def delete_request_material(order_id):
    helper.delete("request_materials", "request_id", order_id)