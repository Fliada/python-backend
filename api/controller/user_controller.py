from fastapi import APIRouter, Depends, HTTPException, status

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
    is_active = userRequest.is_active
    email = userRequest.email
    phone_number = userRequest.phone_number

    flag = user.create_user(password, is_superuser, first_name, last_name, second_name, is_staff, is_active, email,
                            phone_number)
    if flag:
        return 'Пользователь успешно создан'
    return HTTPException(status_code=400, detail="Пользователь НЕ создан")


# Функция для проверки пароля и создания токена
def check_pass_and_create_token(email: str, password: str):
    # Ваша логика для проверки пароля
    usr = user.find_user_by_email(email)
    if usr and usr.check_password(password) and usr.is_active:
        # Создание токена с использованием метода create_token из JWTManager
        token = jwt_manager.create_token(usr.id_, usr.is_superuser, usr.is_staff)
        usr.set_last_login(datetime.now())
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")


@user_routes.post('/auth')
def get_token(userRequest: UserLogin):
    return check_pass_and_create_token(userRequest.email, userRequest.password)


@user_routes.post('/{user_id}')
def ban_user(
        user_id: str,
        current_user: dict = Depends(get_current_user)
):
    if not current_user.get(ROLES.STAFF.value):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can ban users")

    user.ban_user(user_id)
    return 'Забанен пользователь с Id %s' % user_id


@user_routes.post('/{user_id}')
def unban_user(
        user_id: str,
        current_user: dict = Depends(get_current_user)
):
    if not current_user.get(ROLES.STAFF):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can unbun users")

    user.unban_user(user_id)
    return 'Разбанен пользователь с Id %s' % user_id


@user_routes.delete('/{user_id}')
def delete_user(
        user_id: str,
        current_user: dict = Depends(get_current_user)
):
    if current_user.get(ROLES.STAFF) == "False":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only admin and staff can delete users")

    user.delete_user(user_id)
    return 'Удален пользователь с Id %s' % user_id