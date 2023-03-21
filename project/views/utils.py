import jwt
from flask import request, current_app

from project.implemented import user_service
from project import config


def login_required(func):
    def wrapper(*args, **kwargs):
        if not "Authorization" in request.headers:
            return "p", 401
        token = request.headers["Authorization"].split("Bearer ")[-1]
        try:
            data = jwt.decode(token, current_app.config.get("SECRET_KEY"), algorithms=['HS256'])
            user = user_service.get_by_email(data['email'])
            if user:
                return func(*args, **kwargs)
            else:
                return "", 401
        except:
            return "u", 401
    return wrapper