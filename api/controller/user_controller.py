from dataclasses import asdict

from fastapi import APIRouter, Depends, HTTPException, status
from starlette.responses import JSONResponse

from api.ConfigHelper import ConfigHelper
from api.data import user
from api.model.User import UserCreate, UserLogin
from fastapi import HTTPException
from api.JWTManager import JWTManager

from fastapi.security import OAuth2PasswordBearer, HTTPBearer

from api.roles import ROLES
from datetime import datetime

config_helper = ConfigHelper()
secret_key = config_helper.config['JWT']['SECRET_KEY']

user_routes = APIRouter()
jwt_manager = JWTManager(secret_key)

# Создаем экземпляр OAuth2PasswordBearer для извлечения токена из запроса
get_bearer_token = HTTPBearer(auto_error=False)


# Декоратор для проверки наличия и валидности токена
def get_current_user(token: str = Depends(get_bearer_token)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token_bytes = token.credentials
        payload = jwt_manager.verify_token(token_bytes)
        if payload is None:
            raise credentials_exception
        return payload
    except Exception:
        raise credentials_exception


@user_routes.get('/all')
def get_users(
        current_user: dict = Depends(get_current_user)
):
    if not current_user.get(ROLES.ADMIN.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin can get users")

    users = user.get_users()
    return JSONResponse(content=[asdict(usr) for usr in users])


@user_routes.get('/{user_id}')
def get_user(user_id: str, current_user: dict = Depends(get_current_user)):
    usr = user.get_user(user_id)

    if usr:
        return {"sub": usr.id_,
                "is_superuser": usr.is_superuser,
                "is_stuff": usr.is_staff}
    else:
        return {"message": "User not found"}


@user_routes.post('/create')
def insert_user(
        userRequest: UserCreate,
        current_user: dict = Depends(get_current_user)
):
    if not current_user.get(ROLES.STAFF.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can create users")

    is_superuser = userRequest.is_superuser
    is_staff = userRequest.is_staff

    if (is_superuser or is_staff) and not current_user.get(ROLES.ADMIN.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin can create admins and staff")

    # РАБОТАЕТ
    # ШАБЛОН В MODEL.USER.PY
    password = userRequest.password
    first_name = userRequest.first_name
    last_name = userRequest.last_name
    second_name = userRequest.second_name
    email = userRequest.email
    phone_number = userRequest.phone_number

    flag = user.create_user(password, is_superuser, first_name, last_name, second_name, is_staff, email,
                            phone_number)
    if flag:
        return 'Пользователь успешно создан'
    return HTTPException(status_code=400, detail="Пользователь НЕ создан")


# Функция для проверки пароля и создания токена
def check_pass_and_create_token(email: str, password: str):
    # Ваша логика для проверки пароля
    usr = user.find_user_by_email(email)
    if usr and usr.check_password(password) and usr.is_active == "True":
        # Создание токена с использованием метода create_token из JWTManager
        token = jwt_manager.create_token(usr.id_, usr.is_superuser, usr.is_staff)
        usr.set_last_login(datetime.now())
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


@user_routes.post('/auth')
def get_token(userRequest: UserLogin):
    return check_pass_and_create_token(userRequest.email, userRequest.password)


@user_routes.post('/ban/{user_id}')
def ban_user(
        user_id: str,
        current_user: dict = Depends(get_current_user)
):
    try:
        usr = user.find_user_by_id(user_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

    if not current_user.get(ROLES.STAFF.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can ban users")

    if (usr.is_superuser == "True" or usr.is_staff == "True") and not current_user.get(ROLES.ADMIN.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin can ban admins and staff")

    user.ban_user(user_id)
    return 'Забанен пользователь с Id %s' % user_id


@user_routes.post('/unban/{user_id}')
def unban_user(
        user_id: str,
        current_user: dict = Depends(get_current_user)
):
    try:
        usr = user.find_user_by_id(user_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

    if not current_user.get(ROLES.STAFF.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can unban users")

    if (usr.is_superuser == "True" or usr.is_staff == "True") and not current_user.get(ROLES.ADMIN.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin can unban admins and staff")

    user.unban_user(user_id)
    return 'Разбанен пользователь с Id %s' % user_id


@user_routes.delete('/{user_id}')
def delete_user(
        user_id: str,
        current_user: dict = Depends(get_current_user)
):
    try:
        usr = user.find_user_by_id(user_id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")

    if not current_user.get(ROLES.STAFF.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can delete users")

    if (usr.is_superuser == "True" or usr.is_staff == "True") and not current_user.get(ROLES.ADMIN.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin can delete admins and staff")

    user.delete_user(user_id)
    return 'Удален пользователь с Id %s' % user_id
