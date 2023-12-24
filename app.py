from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from api.ConfigHelper import ConfigHelper
from api.controller import user_controller, order_controller, material_controller, address_controller, \
    request_materials_controller, category_controller
from api.data.user import find_user_by_email
from api.model.User import UserLogin

app = FastAPI(openapi_prefix="/")

config_helper = ConfigHelper()
app.secret_key = config_helper.config['APP']['SECRET_KEY']

app.include_router(user_controller.user_routes, prefix="/user", tags=["User"])
app.include_router(order_controller.order_routes, prefix="/order", tags=["Order"])
app.include_router(material_controller.material_routes, prefix="/material", tags=["Materials"])
app.include_router(address_controller.address_routes, prefix="/address", tags=["Address"])
app.include_router(request_materials_controller.request_materials_routes, prefix="/request_material",
                   tags=["Request materials"])
app.include_router(category_controller.category_routes, prefix="/category", tags=["Category"])

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', response_class=FileResponse)
def index():
    return 'resources/templates/index.html'


# @app.post('/authorization')
# def login(user: UserLogin):
#    email = user.email
#    password = user.password
#    print(email)
#    print(password)
#    # РАБОТАЕТ
#    result = find_user_by_email(email)

#    # if user.check_password(user.password) == password:
#    #     # Устанавливаем сессию для пользователя
#    #     session['user_id'] = user.id
#    #     if user.is_superuser:
#    #         session['role'] = 'admin'
#    #     elif user.is_staff:
#    #         session['role'] = 'manager'
#    #     else:
#    #         session['role'] = 'user'
#    #     return "Вход выполнен успешно!"
#    return "Пользователь авторизован"


# @app.post('/logout')
# def logout():
#     session.clear()
#     return render_template('index.html')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8080)
