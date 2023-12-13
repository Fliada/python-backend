import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter


jwt_routes = APIRouter()
tokens = []


@jwt_routes.post('/check')
def check_jwt(jwt_token):
    try:
        # Декодировать JWT
        payload = jwt.decode(jwt_token, "your_secret_key", algorithms=["HS256"])
        return True
    except jwt.exceptions.InvalidTokenError:
        return False


@jwt_routes.post('/generate')
def generate_jwt(email, password):
    for payload in tokens:
        if payload['email'] == email:
            return "User already has token"
    # Установить время действия JWT на 1 час
    expiry_time = datetime.now() + timedelta(hours=1)

    # Создать словарь дляpayload
    payload = {
        'email': '{0}'.format(email),
        'exp': expiry_time
    }

    # Закодировать payload в JWT
    jwt_string = jwt.encode(payload, 'your_secret_key', algorithm='HS256')
    # заносим юзера в список
    tokens.append(payload)
    return jwt_string