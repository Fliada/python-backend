from dataclasses import dataclass

from api.db.DBHelper import DBHelper

helper = DBHelper()


@dataclass
class Request:
    request_id: str
    material_id: str
    count: int

    def __init__(self, request_id, material_id, count):
        self.request_id = request_id
        self.material_id = material_id
        self.count = count


def create_request_material(request_id, material_id, count):
    params = ["request_id", "material_id", "count"]

    args = [
        request_id,
        material_id,
        count
    ]

    helper.insert("request_materials", params, args)


def get_all_request_material(order_id):
    req = f"select * from request_materials r where request_id = '{order_id}'"
    lines = helper.any_request(req)

    categories = []

    for l in lines:
        categories.append(
            Request(*l)
        )

    print(categories)
    return categories


def delete_request_material(order_id):
    helper.delete("request_materials", "request_id", order_id)