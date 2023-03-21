from marshmallow import Schema, fields
from sqlalchemy import Column, String

from project.dao.model import model


class Genre(model.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
