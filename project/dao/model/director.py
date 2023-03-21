from marshmallow import Schema, fields
from sqlalchemy import Column, String

from project.dao.model import model


class Director(model.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
