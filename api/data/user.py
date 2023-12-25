from dataclasses import dataclass

from werkzeug.security import generate_password_hash, check_password_hash
from api.db.DBHelper import DBHelper
from datetime import datetime
from api.DateHelper import format_date

helper = DBHelper()


@dataclass
class auth_user:
    id_: int
    password: str
    last_login: str
    is_superuser: bool
    first_name: str
    last_name: str
    second_name: str
    is_staff: bool
    is_active: bool
    date_joined: datetime
    email: str
    phone_number: str

    def __init__(self, id_: int, password: str, last_login: str, is_superuser: bool, first_name: str, last_name: str,
                 second_name: str, is_staff: bool, is_active: bool, date_joined: str, email: str, phone_number: str):
        self.id_ = id_
        self.password = password
        self.last_login = last_login
        self.is_superuser = is_superuser
        self.first_name = first_name
        self.last_name = last_name
        self.second_name = second_name
        self.is_staff = is_staff
        self.is_active = is_active
        self.date_joined = date_joined
        self.email = email
        self.phone_number = phone_number

    def set_password(self, password):
        self.password = generate_password_hash(password=password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_last_login(self, curr: datetime):
        self.last_login = format_date(curr)
        helper.update("auth_user", "id", self.id_, "last_login", self.last_login)


def create_user(password, is_superuser, first_name, last_name, second_name, is_staff, email, phone_number):
    params = ["password", "last_login", "is_superuser", "first_name", "last_name",
              "second_name", "is_staff", "is_active", "date_joined", "email", "phone_number"]

    now = datetime.now()

    args = [
        generate_password_hash(password=password),
        format_date(now),
        is_superuser,
        first_name,
        last_name,
        second_name,
        is_staff,
        True,
        format_date(now),
        email,
        phone_number
    ]

    flag = helper.insert("auth_user", params, args)
    if flag:
        return find_user_by_email(email)

    return flag


def get_user(_id):
    line = helper.get("auth_user", ["id"], [_id])
    print(line)

    if len(line) == 0:
        return None

    usr = auth_user(*line[0])
    return usr


def get_users():
    lines = helper.print_info("auth_user")

    users = []

    for l in lines:
        users.append(
            auth_user(*l)
        )

    return users


def delete_user(_id):
    helper.delete("auth_user", "id", _id)


def ban_user(_id):
    helper.update("auth_user", "id", _id, "is_active", "False")


def unban_user(_id):
    helper.update("auth_user", "id", _id, "is_active", "True")


def find_user_by_id(_id):
    line = helper.get("auth_user", ["id"], [_id])[0]
    user = auth_user(*line)

    return user


def find_user_by_email(email):
    line = helper.get("auth_user", ["email"], [email])[0]

    if len(line) == 0:
        return None

    user = auth_user(*line)

    return user
