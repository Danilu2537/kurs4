from contextlib import suppress
from typing import Any, Dict, List

from sqlalchemy.exc import IntegrityError

from project.config import config
from project.dao.model.director import Director
from project.dao.model.genre import Genre
from project.dao.model.movie import Movie
from project.setup_db import db
from project.utils import read_json
from run import create_app


def load_data(data: List[Dict[str, Any]], model) -> None:
    for item in data:
        item['id'] = item.pop('pk')
        db.session.add(model(**item))


if __name__ == '__main__':
    fixtures: Dict[str, List[Dict[str, Any]]] = read_json('fixtures.json')

    app = create_app(config)

    with app.app_context():
        # TODO: [fixtures] Добавить модели Directors и Movies
        load_data(fixtures['directors'], Director)
        load_data(fixtures['movies'], Movie)
        load_data(fixtures['genres'], Genre)

        with suppress(IntegrityError):
            db.session.commit()
