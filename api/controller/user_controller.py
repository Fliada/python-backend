from flask import Blueprint
from flask import Flask, request, session
from api.data import user


user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return 'Get user with Id %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ (ОН ВООБЩЕ НУЖЕН??)
@user_routes.route('/user/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    return 'Put user with Id %d' % user_id


@user_routes.route('/user/create', methods=['POST'])
def insert_user():
    if session['role'] == 'admin':
        data = request.get_json()

        password = data.get('password')
        is_superuser = data.get('is_superuser')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        second_name = data.get('second_name')
        is_staff = data.get('is_staff')
        is_active = data.get('is_active')
        email = data.get('email')
        user.create_user(password, is_superuser, first_name, last_name, second_name, is_staff, is_active, email)
        return 'Пользователь создан'
    else:
        return "Недостаточно прав"


@user_routes.route('/user/<int:user_id>', methods=['POST', 'PUT'])
def ban_user(user_id):
    if (session['role'] == 'admin') | (session['role'] == 'manager'):
        user.ban_user(user_id)
        return 'Забанен пользователь с Id %d' % user_id
    else:
        return "Недостаточно прав"


@user_routes.route('/user/<int:user_id>', methods=['POST', 'PUT'])
def unban_user(user_id):
    if (session['role'] == 'admin') | (session['role'] == 'manager'):
        user.unban_user(user_id)
        return 'Разбанен пользователь с Id %d' % user_id
    else:
        return "Недостаточно прав"


@user_routes.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if session['role'] == 'admin':
        return 'Удален пользователь с Id %d' % user_id
    else:
        return "Недостаточно прав"

