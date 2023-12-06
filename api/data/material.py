from api.db.DBHelper import DBHelper

helper = DBHelper()


class Material:
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
    material = Material(
        line[0], line[1], line[2], line[3]
    )
    return material


def delete_material(_id):
    helper.delete("material", ["id"], [_id])
