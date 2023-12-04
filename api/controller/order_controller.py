from flask import Blueprint

order = Blueprint('order_routes', __name__)


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order.route('/order/<int:order_id>', methods=['POST'])
def post_order(order_id):
    return 'Order %d' % order_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return 'Order %d' % order_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order.route('/order/<int:post_id>', methods=['PUT'])
def put_order(post_id):
    return 'Order %d' % post_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order.route('/order/repeat/<int:post_id>', methods=['POST'])
def repeat_order(post_id):
    return 'Repeat order %d' % post_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@order.route('/order/<int:post_id>', methods=['DELETE'])
def delete_order(post_id):
    return 'Order %d' % post_id

