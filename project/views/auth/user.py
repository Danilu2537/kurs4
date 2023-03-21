import jwt
from flask import request, current_app
from flask_restx import Namespace, Resource

from project import config
from project.dao.model.user import UserSchema
from project.implemented import user_service
from project.views.utils import login_required

user_ns = Namespace('user')


@user_ns.route('/')
class User(Resource):
    @login_required
    def get(self):
        token = request.headers["Authorization"].split("Bearer ")[-1]
        try:
            data = jwt.decode(token, current_app.config.get("SECRET_KEY"), algorithms=['HS256'])
            user = user_service.get_by_email(data['email'])
            if user:
                return UserSchema().dump(user), 200
            else:
                return "", 401
        except:
            return "", 401

    @login_required
    def patch(self):
        req_json = request.json
        req_json["id"] = uid
        user_service.partially_update(req_json)
        return "", 204

    @login_required
    def put(self):
        req_json = request.json
        req_json["id"] = uid
        user_service.update(req_json)
        return "", 204
