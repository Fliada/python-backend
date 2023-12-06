from api.db.DBHelper import DBHelper

helper = DBHelper()


class Request:
    def __init__(self, id_, user_id, staff_id, address_id, comment, status_id,
                 date_creation, date_selected, date_actual):
        self.id_ = id_
        self.user_id = user_id
        self.staff_id = staff_id
        self.address_id = address_id
        self.comment = comment
        self.status_id = status_id
        self.date_creation = date_creation
        self.date_selected = date_selected
        self.date_actual = date_actual


def create_request(user_id, address_id, comment, date_selected):
    params = ["user_id", "staff_id", "address_id", "comment", "status_id", "date_creation",
              "date_selected", "date_actual"]

    date_creation = datetime.datetime.now()

    args = [
        user_id,
        None,
        address_id,
        comment,
        0,
        date_creation,
        date_selected,
        None
    ]

    helper.insert("request", params, args)

    return find_request_by_unique(user_id, date_creation)


def find_request_by_unique(user_id, date_creation):
    line = helper.get("request", ["user_id", "date_creation"], [user_id, date_creation])
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

    requests = []

    for l in lines:
        requests.append(
            Request(
                line[0], line[1], line[2],
                line[3], line[4], line[5],
                line[6], line[7], line[8]
            )
        )

    return requests