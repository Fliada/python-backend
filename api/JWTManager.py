import jwt
from datetime import datetime, timedelta


class JWTManager:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create_token(self, user_id, is_superuser=False, is_staff=False, expiration_minutes=30):
        now = datetime.utcnow()
        payload = {
            'sub': user_id,
            'is_superuser': is_superuser,
            'is_staff': is_staff,
            'iat': now,
            'exp': now + timedelta(minutes=expiration_minutes)
        }
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def verify_token(self, token):
        # Метод проверки подписи и срока действия JWT
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            # Токен истек
            return None
        except jwt.InvalidTokenError:
            # Некорректный токен
            return None

    def refresh_token(self, old_token, expiration_minutes=30):
        # Метод обновления токена
        payload = self.verify_token(old_token)
        if payload:
            user_id = payload['sub']
            return self.create_token(user_id, expiration_minutes)
        return None

    def invalidate_token(self, token):
        # Метод инвалидации токена (пример: добавление в черный список)
        pass
