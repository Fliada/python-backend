from dataclasses import dataclass

from api.db.DBHelper import DBHelper

helper = DBHelper()


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
    material = Material(*line[0])

    return material


def delete_material(_id):
    helper.delete("material", ["id"], [_id])
