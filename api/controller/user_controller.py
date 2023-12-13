import requests
from fastapi import FastAPI, Request, APIRouter
from flask import request
from api.data import user
from api.model.User import UserCreate
from fastapi import HTTPException
from api.controller import jwt_controller

user_routes = APIRouter()


@user_routes.get('/{user_id}')
def get_user(user_id: str):
    return user.get_user(user_id)


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


@user_routes.post('/try_login')
def check_pass():
    data = request.get_json()
    usr = user.find_user_by_email(data.get('email'))
    if usr is None:
        raise HTTPException(status_code=404, detail="User not found")
    elif not usr.check_password(data.get('pass')):
        raise HTTPException(status_code=400, detail="Invalid password")
    else:
        return {"jwt": jwt_controller.generate(data.get('email'))}


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