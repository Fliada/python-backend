from flask import Blueprint

user = Blueprint('user_routes', __name__)


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@user.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return 'Get user with Id %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@user.route('/user/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    return 'Put user with Id %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ БАНА ПОЛЬЗОВАТЕЛЯ
@user.route('/user/<int:user_id>', methods=['POST', 'PUT'])
def ban_user(user_id):
    return 'Ban user with Id %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@user.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return 'Delete user with Id %d' % user_id
