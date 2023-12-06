from flask import Blueprint
from flask import Flask, request
from api.data.user import create_user, get_user
import requests


user = Blueprint('user_routes', __name__)


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@user.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return 'Get user with Id %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@user.route('/user/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    return 'Put user with Id %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@user.route('/user/create', methods=['POST'])
def insert_user():
    data = request.get_json()

    password = data.get('password')
    is_superuser = data.get('is_superuser')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    second_name = data.get('second_name')
    is_staff = data.get('is_staff')
    is_active = data.get('is_active')
    email = data.get('email')
    create_user(password, is_superuser, first_name, last_name, second_name, is_staff, is_active, email)
    return 'Create user'


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ БАНА ПОЛЬЗОВАТЕЛЯ
@user.route('/user/<int:user_id>', methods=['POST', 'PUT'])
def ban_user(user_id):
    return 'Ban user with Id %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@user.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return 'Delete user with Id %d' % user_id
