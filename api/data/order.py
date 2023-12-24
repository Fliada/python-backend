import datetime
from dataclasses import dataclass
from typing import List

from api.data import request_materials
from api.data.request_materials import Request_material
from api.db.DBHelper import DBHelper
from datetime import datetime
from api.DateHelper import format_date

import json

helper = DBHelper()


@dataclass
class Request:
    id_: int
    user_id: int
    user_first_name: str
    user_last_name: str
    user_second_name: str
    staff_id: int
    address: str
    comment: str
    status_id: int
    date_creation: str
    date_selected: str
    date_actual: str
    materials: List[Request_material]

    def __init__(self, id_, user_id, user_first_name, user_last_name, user_second_name, staff_id, address, comment, status_id,
                 date_creation, date_selected, date_actual):
        self.id_ = id_
        self.user_id = user_id
        self.staff_id = staff_id
        self.address = address
        self.comment = comment
        self.status_id = status_id
        self.date_creation = date_creation
        self.date_selected = date_selected
        self.date_actual = date_actual
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_second_name = user_second_name

    def set_materials(self, mats: List[Request_material]):
        self.materials = mats


def create_request(user_id: int, address: str, comment: str, date_selected: datetime):
    params = ["user_id", "staff_id", "address", "comment", "status_id", "date_creation",
              "date_selected", "date_actual"]

    date_creation = datetime.now()

    args = [
        user_id,
        None,
        address,
        comment,
        1,
        format_date(date_creation),
        format_date(date_selected),
        None
    ]

    helper.insert("request", params, args)


def get_request(_id):
    req = f"SELECT r.id, r.user_id, au.first_name, au.last_name, au.second_name, " \
          f"r.staff_id, r.address, r.comment, r.status_id, r.date_creation, " \
          f"r.date_selected, r.date_actual " \
          f"FROM request r JOIN auth_user au " \
          f"ON r.user_id = au.id " \
          f"WHERE r.id = '{_id}'"

    line = helper.any_request(req)[0]
    print(line)

    req = Request(*line)
    req.set_materials(request_materials.get_all_request_material(_id))

    return req


def get_user_request(user_id):

    req = f"SELECT r.id, r.user_id, au.first_name, au.last_name, au.second_name, " \
          f"r.staff_id, r.address, r.comment, r.status_id, r.date_creation, " \
          f"r.date_selected, r.date_actual  " \
          f"FROM request r JOIN auth_user au " \
          f"ON r.user_id = au.id " \
          f"WHERE r.user_id = '{user_id}' " \
          f"ORDER BY r.status_id"

    lines = helper.any_request(req)

    requests = []

    for l in lines:
        req = Request(*l)
        req.set_materials(request_materials.get_all_request_material(user_id))
        requests.append(req)

    print(requests)
    return requests


def update_request(_id, item, name):
    line = helper.update("request", ["id"], [_id],  column_change=item, change=name)
    print(line)
    return line


def delete_request(_id):
    helper.delete("request", "id", _id)


def find_request_by_unique(_id):
    line = helper.any_request("SELECT * FROM request r WHERE user_id = 1 ORDER BY r.date_creation DESC")[0]
    request = Request(*line)

    return request


def find_request_by_id(_id):
    line = helper.get("request", ["id"], [_id])[0]
    request = Request(*line)

    return request


def get_all_requests():

    req = f"SELECT r.id, r.user_id, au.first_name, au.last_name, au.second_name, " \
          f"r.staff_id, r.address, r.comment, r.status_id, r.date_creation, " \
          f"r.date_selected, r.date_actual  " \
          f"FROM request r JOIN auth_user au " \
          f"ON r.user_id = au.id " \
          f"ORDER BY r.status_id"

    lines = helper.any_request(req)

    print(lines)

    requests = []

    for l in lines:
        req = Request(*l)
        req.set_materials(request_materials.get_all_request_material(l[0]))
        requests.append(req)

    print(requests)
    return requests


def convert_requests_to_json(requests):
    return json.dumps([req.to_dict() for req in requests], indent=2)