from fastapi import FastAPI, Request
from fastapi.responses import FileResponse

from api.controller import user_controller, order_controller, material_controller, address_controller
from api.data.user import find_user_by_email
from api.model.User import UserLogin

app = FastAPI()
app.secret_key = "122333444455555666666777777788888888999999999"
app.include_router(user_controller.user_routes, prefix="/user", tags=["User"])
app.include_router(order_controller.order_routes, prefix="/order", tags=["Order"])
app.include_router(material_controller.material_routes, prefix="/materials", tags=["Materials"])
app.include_router(address_controller.address_routes, prefix="/address", tags=["Address"])


@app.get('/', response_class=FileResponse)
def index():
    return 'resources/templates/index.html'


@app.post('/authorization')
def login(user: UserLogin):
    email = user.email
    password = user.password
    print(email)
    print(password)
    # РАБОТАЕТ
    result = find_user_by_email(email)

    # if user.check_password(user.password) == password:
    #     # Устанавливаем сессию для пользователя
    #     session['user_id'] = user.id
    #     if user.is_superuser:
    #         session['role'] = 'admin'
    #     elif user.is_staff:
    #         session['role'] = 'manager'
    #     else:
    #         session['role'] = 'user'
    #     return "Вход выполнен успешно!"
    return "Пользователь авторизован"


# @app.post('/logout')
# def logout():
#     session.clear()
#     return render_template('index.html')


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8080)
