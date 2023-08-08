from flask_restx import Model, fields

from project.setup.api import api

genre: Model = api.model(
    'Жанр',
    {
        'id': fields.Integer(required=True, example=1),
        'name': fields.String(required=True, max_length=100, example='Комедия'),
    },
)
