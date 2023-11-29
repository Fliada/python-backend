from app import app


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return 'Post %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/user/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    return 'Post %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ БАНА ПОЛЬЗОВАТЕЛЯ
@app.route('/user/<int:user_id>', methods=['PUT'])
def ban_user(user_id):
    return 'Post %d' % user_id


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return 'Post %d' % user_id