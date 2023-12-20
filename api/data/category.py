from dataclasses import dataclass

from api.db.DBHelper import DBHelper

helper = DBHelper()


@dataclass
class Category:
    id_: str
    name: str

    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name


def get_category(_id):
    line = helper.get("category", ["id"], [_id])
    print(line)
    category = Category(*line[0])

    return category


def get_all_categories():
    req = f"SELECT *" \
          f"FROM category"
    lines = helper.any_request(req)

    categories = []

    for l in lines:
        categories.append(
            l
        )

    print(categories)
    return categories
