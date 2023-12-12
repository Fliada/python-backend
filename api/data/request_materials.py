from api.db.DBHelper import DBHelper

helper = DBHelper()


class Request:
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
