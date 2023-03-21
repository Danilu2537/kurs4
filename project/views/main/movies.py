from flask import request
from flask_cors import cross_origin
from flask_restx import Resource, Namespace

from project.dao.model.movie import MovieSchema
from project.implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @cross_origin()
    def get(self):
        """Метод с пагинацией по 12 записей на page,
        если есть status=new, возвращаем фильмы отсортированные по новизне"""
        page = request.args.get('page')
        if page:
            page = int(page)
        status = request.args.get('status')
        if status == 'new':
            movies = movie_service.get_new(page)
        else:
            movies = movie_service.get_all(page)
        return MovieSchema(many=True).dump(movies), 200

    def post(self):
        req_json = request.json
        ent = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{ent.id}"}


@movie_ns.route('/<int:bid>/')
class MovieView(Resource):
    @cross_origin()
    def get(self, bid):
        movie = movie_service.get_one(bid)
        return MovieSchema().dump(movie), 200

    def put(self, bid):
        req_json = request.json
        req_json["id"] = bid
        movie_service.update(req_json)
        return "", 204

    def patch(self, bid):
        req_json = request.json
        req_json["id"] = bid
        movie_service.partially_update(req_json)
        return "", 204

    def delete(self, bid):
        movie_service.delete(bid)
        return "", 204
