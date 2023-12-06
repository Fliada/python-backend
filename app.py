from flask import Flask, render_template, session, request

from api.controller.order_controller import order_routes
from api.controller.user_controller import user_routes

from api.data.user import find_user_by_email

app = Flask(__name__, template_folder='resources/templates')
app.secret_key = "122333444455555666666777777788888888999999999"
app.register_blueprint(user_routes)  # Мб добавить сюда url_prefix='/user' а в файле убрать все
app.register_blueprint(order_routes)  # Мб добавить сюда url_prefix='/order' а в файле убрать все


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/authorization', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.json.get('email')
        password = request.json.get('pass')

        # Проверяем наличие пользователя в базе данных
        user = find_user_by_email(email)
        if user.check_password(user.password) == password:
            # Устанавливаем сессию для пользователя
            session['user_id'] = user.id
            if user.is_superuser:
                session['role'] = 'admin'
            elif user.is_staff:
                session['role'] = 'manager'
            else:
                session['role'] = 'user'
            return "Вход выполнен успешно!"
        return "Неправильный логин или пароль"
    return render_template('index.html')


@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
