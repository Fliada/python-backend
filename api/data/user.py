import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from api.db.DBHelper import DBHelper

helper = DBHelper()


class auth_user:
    def __init__(self, id_, password, last_login, is_superuser, first_name, last_name,
                 second_name, is_staff, is_active, date_joined, email, phone_number):
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


def create_user(password, is_superuser, first_name, last_name, second_name, is_staff, is_active, email, phone_number):
    params = ["password", "last_login", "is_superuser", "first_name", "last_name",
              "second_name", "is_staff", "is_active", "date_joined", "email", "phone_number"]

    args = [
        generate_password_hash(password=password),
        datetime.datetime.now(),
        is_superuser,
        first_name,
        last_name,
        second_name,
        is_staff,
        is_active,
        datetime.datetime.now(),
        email,
        phone_number
    ]

    helper.insert("auth_user", params, args)

    return find_user_by_email(email)


def get_user(_id):
    line = helper.get("auth_user", ["id"], [_id])
    print(line)

    if len(line) == 0:
        return None

    usr = auth_user(*line[0])
    return usr


def delete_user(_id):
    helper.delete("auth_user", ["id"], [_id])


def ban_user(_id):
    helper.update("auth_user", ["id"], [_id], "is_active", "false")


def unban_user(_id):
    helper.update("auth_user", ["id"], [_id], "is_active", "true")


def find_user_by_id(_id):
    line = helper.get("auth_user", ["id"], [_id])[0]
    user = auth_user(
        line[0], line[1], line[2], line[3],
        line[4], line[5], line[6], line[7],
        line[8], line[9], line[10], line[11]
    )

    return user


def find_user_by_email(email):
    line = helper.get("auth_user", ["email"], [email])[0]
    user = auth_user(
        line[0], line[1], line[2], line[3],
        line[4], line[5], line[6], line[7],
        line[8], line[9], line[10], line[11]
    )

    return user