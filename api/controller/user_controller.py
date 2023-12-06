from flask import Blueprint, request
from api.data import user

user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/user', methods=['POST'])
def create_user():
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    second_name = request.json.get('second_name')

    password = request.json.get('password')
    email = request.json.get('email')

    is_superuser = request.json.get('is_superuser')
    is_staff = request.json.get('is_staff')
    is_active = request.json.get('is_active')

    user.create_user(password, is_superuser, first_name, last_name, second_name, is_staff, is_active, email)


@user_routes.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user.find_user_by_id(user_id)


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@user_routes.route('/user/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    return 'Put user with Id %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ БАНА ПОЛЬЗОВАТЕЛЯ
@user_routes.route('/user/<int:user_id>', methods=['POST', 'PUT'])
def ban_user(user_id):
    return 'Ban user with Id %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@user_routes.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return 'Delete user with Id %d' % user_id
