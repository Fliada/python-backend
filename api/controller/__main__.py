from app import app


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/user', methods=['GET'])
def get_user(user_id):
    return 'Users'


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/order', methods=['GET'])
def get_order(user_id):
    return 'Orders'


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/', methods=['GET'])
def get_resource(user_id):
    return 'Resources'


# TODO СДЕЛАТЬ РЕАЛИЗАЦИЮ
@app.route('/status', methods=['GET'])
def status():
    return "Statuses"
