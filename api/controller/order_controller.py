from app import app


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return 'Post %d' % order_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return 'Post %d' % order_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/order/<int:post_id>', methods=['PUT'])
def put_order(post_id):
    return 'Post %d' % post_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/order/<int:post_id>', methods=['DELETE'])
def delete_order(post_id):
    return 'Post %d' % post_id

