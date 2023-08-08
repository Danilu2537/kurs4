import datetime
import hashlib

import jwt
from flask import current_app

from project.config import BaseConfig


class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service

    def get_hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, user_d):
        user_d['password'] = self.get_hash(user_d['password'])
        return self.user_service.create(user_d)

    def login(self, user_d):
        """При удачной аутентификации функция возвращает access_token и refresh_token"""
        user_d['password'] = self.get_hash(user_d['password'])
        user = self.user_service.get_by_email_and_password(
            user_d['email'], user_d['password']
        )
        if user:
            return self.get_tokens(user)
        else:
            return None

    def get_tokens(self, user):
        data = {'email': user.email}
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = min30
        access_token = jwt.encode(
            data, current_app.config.get('SECRET_KEY'), algorithm='HS256'
        )
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = days130
        refresh_token = jwt.encode(
            data, current_app.config.get('SECRET_KEY'), algorithm='HS256'
        )
        return {'access_token': access_token, 'refresh_token': refresh_token}

    def refresh(self, tokens):
        refresh_token = tokens['refresh_token']
        try:
            data = jwt.decode(
                refresh_token, BaseConfig.SECRET_KEY, algorithms=['HS256']
            )
            user = self.user_service.get_by_email(data['email'])
            if user:
                return self.get_tokens(user)
            else:
                return None
        except Exception:
            return None
