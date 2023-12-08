from fastapi import FastAPI, Request, APIRouter
from api.data import user
from api.model.User import UserCreate

user_routes = APIRouter()


@user_routes.get('/user/<int:user_id>')
def get_user(user_id):
    return 'Get user with Id %d' % user_id


@user_routes.post('/user/create')
def insert_user(userRequest: UserCreate):
    print((userRequest.password, userRequest.is_superuser,
                     userRequest.first_name, userRequest.last_name,
                     userRequest.second_name, userRequest.is_staff,
                     userRequest.is_active, userRequest.email,
                     userRequest.phone_number))

    # ТУТ ТОЖЕ САМОЕ ЧТО И С ДРУГИМ ЗАПРОСОМ В APP.PY ДАННЫЕ ПРИХОДЯТ И ПРАВИЛЬНО ОБРАБАТЫВАЮТСЯ, НО НЕ ДОБАВЛЯЮТСЯ, ЭТО УЖЕ НЕ СЕЙЧАС ДЕЛАЕТСЯ
    # ШАБЛОН ТАКЖЕ В MODEL.USER.PY
    user.create_user(userRequest.password, userRequest.is_superuser,
                     userRequest.first_name, userRequest.last_name,
                     userRequest.second_name, userRequest.is_staff,
                     userRequest.is_active, userRequest.email,
                     userRequest.phone_number)
    return 'Пользователь создан'


@user_routes.post('/user/<int:user_id>')
def ban_user(user_id):
    if (session['role'] == 'admin') | (session['role'] == 'manager'):
        user.ban_user(user_id)
        return 'Забанен пользователь с Id %d' % user_id
    else:
        return "Недостаточно прав"


@user_routes.post('/user/<int:user_id>')
def unban_user(user_id):
    if (session['role'] == 'admin') | (session['role'] == 'manager'):
        user.unban_user(user_id)
        return 'Разбанен пользователь с Id %d' % user_id
    else:
        return "Недостаточно прав"


@user_routes.delete('/user/<int:user_id>')
def delete_user(user_id):
    if session['role'] == 'admin':
        user.delete_user(user_id)
        return 'Удален пользователь с Id %d' % user_id
    else:
        return "Недостаточно прав"
