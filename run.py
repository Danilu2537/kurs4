from project.config import config
from project.dao.model.genre import Genre
from project.dao.model.director import Director
from project.dao.model.movie import Movie
from project.dao.model.user import User






from flask import Flask, jsonify
from flask_cors import CORS

from project.exceptions import BaseServiceError
from project.setup.api import api
from project.setup_db import db
from project.views.auth.auth import auth_ns
from project.views.auth.user import user_ns
from project.views.main.directors import director_ns
from project.views.main.genres import genre_ns
from project.views.main.movies import movie_ns


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)

    db.init_app(app)
    api.init_app(app)
    cors = CORS(app=app)
    app.config['CORS_HEADERS'] = 'Content-Type'


    # Регистрация эндпоинтов
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)

    return app
app = create_app(config)
@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "Director": Director,
        "Movie": Movie,
        "User": User
    }