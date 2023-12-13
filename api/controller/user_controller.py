from fastapi import FastAPI, Request, APIRouter
from api.data import user
from api.model.User import UserCreate

user_routes = APIRouter()


@user_routes.get('/{user_id}')
def get_user(user_id: str):
    return 'Get user with Id %s' % user_id


@user_routes.post('/create')
def insert_user(userRequest: UserCreate):
    print(userRequest.password, userRequest.is_superuser,
          userRequest.first_name, userRequest.last_name,
          userRequest.second_name, userRequest.is_staff,
          userRequest.is_active, userRequest.email,
          userRequest.phone_number)

    # РАБОТАЕТ
    # ШАБЛОН В MODEL.USER.PY
    password = userRequest.password
    is_superuser = userRequest.is_superuser
    first_name = userRequest.first_name
    last_name = userRequest.last_name
    second_name = userRequest.second_name
    is_staff = userRequest.is_staff
    is_active = userRequest.is_active
    email = userRequest.email
    phone_number = userRequest.phone_number

    user.create_user(password, is_superuser, first_name, last_name, second_name, is_staff, is_active, email, phone_number)
    return 'Пользователь создан'


@user_routes.post('/{user_id}')
def ban_user(user_id: str):
    user.ban_user(user_id)
    return 'Забанен пользователь с Id %s' % user_id


@user_routes.post('/{user_id}')
def unban_user(user_id: str):
    user.unban_user(user_id)
    return 'Разбанен пользователь с Id %s' % user_id


@user_routes.delete('/{user_id}')
def delete_user(user_id: str):
    user.delete_user(user_id)
    return 'Удален пользователь с Id %s' % user_id
