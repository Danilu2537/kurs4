import jwt
from flask import current_app, request

from project.implemented import user_service


def login_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return 'p', 401
        token = request.headers['Authorization'].split('Bearer ')[-1]
        try:
            data = jwt.decode(
                token, current_app.config.get('SECRET_KEY'), algorithms=['HS256']
            )
            user = user_service.get_by_email(data['email'])
            if user:
                return func(*args, **kwargs)
            else:
                return 'Error', 401
        except Exception:
            return 'Error', 401

    return wrapper
