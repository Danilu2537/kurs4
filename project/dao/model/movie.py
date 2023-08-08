from marshmallow import Schema, fields
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from project.dao.model import model
from project.dao.model.director import Director, DirectorSchema
from project.dao.model.genre import Genre, GenreSchema


class Movie(model.Base):
    __tablename__ = 'movies'

    title = Column(String(100), nullable=False)
    year = Column(Integer(), nullable=False)
    description = Column(String(1000), nullable=False)
    trailer = Column(String(100), nullable=False)
    rating = Column(Float(), nullable=False)
    genre_id = Column(Integer(), ForeignKey(Genre.id), nullable=False)
    genre = relationship('Genre')
    director_id = Column(Integer(), ForeignKey(Director.id), nullable=False)
    director = relationship('Director')


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)
