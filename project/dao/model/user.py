from marshmallow import Schema, fields
from sqlalchemy import Column, String

from project.dao.model import model


class User(model.Base):
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(200), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    favourite_genre = Column(String(100))


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favourite_genre = fields.Str()
