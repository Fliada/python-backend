import datetime
from dataclasses import dataclass

from api.db.DBHelper import DBHelper
from datetime import datetime
from api.DateHelper import format_date

import json

helper = DBHelper()


@dataclass
class Request:
    id_: int
    user_id: int
    staff_id: int
    address: str
    comment: str
    status_id: int
    date_creation: str
    date_selected: str
    date_actual: str

    def __init__(self, id_, user_id, staff_id, address, comment, status_id,
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
    line = helper.get("request", ["id"], [_id])[0]
    print(line)
    return Request(*line)


def get_user_request(user_id):
    lines = helper.get("request", ["user_id"], [user_id])

    requests = []

    for l in lines:
        requests.append(
            Request(
                l[0], l[1], l[2],
                l[3], l[4], l[5],
                l[6], l[7], l[8]
            )
        )

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
    request = Request(
        line[0], line[1], line[2],
        line[3], line[4], line[5],
        line[6], line[7], line[8]
    )

    return request


def find_request_by_id(_id):
    line = helper.get("request", ["id"], [_id])[0]
    request = Request(
        line[0], line[1], line[2],
        line[3], line[4], line[5],
        line[6], line[7], line[8]
    )

    return request


def get_all_requests():
    lines = helper.print_info("request")
    print(lines)

    requests = []

    for l in lines:
        requests.append(
            Request(*l)
        )

    print(requests)
    return requests


def convert_requests_to_json(requests):
    return json.dumps([req.to_dict() for req in requests], indent=2)