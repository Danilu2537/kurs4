from flask import request
from flask_cors import cross_origin
from flask_restx import Namespace, Resource

from project.dao.model.director import DirectorSchema
from project.implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @cross_origin()
    def get(self):
        """Метод с пагинацией по 12 записей на page"""
        page = request.args.get('page')
        if page:
            page = int(page)
        directors = director_service.get_all(page)
        return DirectorSchema(many=True).dump(directors), 200

    def post(self):
        req_json = request.json
        ent = director_service.create(req_json)
        return '', 201, {'location': f'/directors/{ent.id}'}


@director_ns.route('/<int:bid>/')
class DirectorView(Resource):
    def get(self, bid):
        director = director_service.get_one(bid)
        return DirectorSchema().dump(director), 200

    def put(self, bid):
        req_json = request.json
        req_json['id'] = bid
        director_service.update(req_json)
        return '', 204

    def patch(self, bid):
        req_json = request.json
        req_json['id'] = bid
        director_service.partially_update(req_json)
        return '', 204

    def delete(self, bid):
        director_service.delete(bid)
        return '', 204
