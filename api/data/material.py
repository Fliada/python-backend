from dataclasses import dataclass

from api.db.DBHelper import DBHelper

helper = DBHelper()
import json


@dataclass
class Material:
    id_: int
    category_id: int
    name: str
    units: str

    def __init__(self, id_, category_id, name, units):
        self.id_ = id_
        self.category_id = category_id
        self.name = name
        self.units = units


def create_material(category_id, name, units):
    params = ["category_id", "name", "units"]

    args = [
        category_id,
        name,
        units
    ]

    helper.insert("material", params, args)


def get_material(_id):
    line = helper.get("material", ["id"], [_id])
    print(line)
    mat = Material(*line[0])

    return mat


def get_all_materials():
    req = f"SELECT m.id, c.name, m.name, m.units " \
          f"FROM material m JOIN category c ON m.category_id = c.id"
    lines = helper.any_request(req)
    print(lines)

    materials = []

    for l in lines:
        materials.append(
            Material(*l)
        )

    print(materials)
    return materials


def delete_material(_id):
    helper.delete("material", ["id"], [_id])


def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4, ensure_ascii=False)
