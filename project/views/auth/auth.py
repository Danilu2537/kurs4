from flask import request
from flask_restx import Namespace, Resource

from project.implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class Register(Resource):
    def post(self):
        req_json = request.json
        auth_service.register(req_json)
        return "", 201


@auth_ns.route('/login/')
class Login(Resource):
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        if None in (email, password):
            return "Required params: email, password", 400
        req_json = request.json
        tokens = auth_service.login(req_json)
        if tokens:
            return tokens, 200
        else:
            return "Incorrect password or email", 401

    def put(self):
        req_json = request.json
        tokens = auth_service.refresh(req_json)
        if tokens:
            return tokens, 200
        else:
            return "", 401
