from flask import Flask, render_template

from api.controller.order_controller import order
from api.controller.user_controller import user

app = Flask(__name__, template_folder='resources/templates')
app.register_blueprint(user)  # Мб добавить сюда url_prefix='/user' а в файле убрать все
app.register_blueprint(order)  # Мб добавить сюда url_prefix='/order' а в файле убрать все


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()