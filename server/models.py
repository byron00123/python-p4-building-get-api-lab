from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Float

from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    baked_goods = relationship('BakedGood', backref='bakery', cascade='all, delete-orphan')

class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'

    id = Column(Integer, primary_key=True)
    name = Column(String)  # Add the name attribute
    bakery_id = Column(Integer, ForeignKey('bakeries.id'))
    price = Column(Float)

