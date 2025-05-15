import datetime
import enum

import sqlalchemy
from core.app.extensions import db


class ProductCategory(enum.Enum):
    boats = "лодки"
    fishing_line = "лески"
    lines_reels = "катушки"
    fishing_rods = "удочки"
    hooks = "крючки"


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )
    picture1 = db.Column(
        db.String(200),
        nullable=True,
    )
    picture2 = db.Column(
        db.String(200),
        nullable=True,
    )
    picture3 = db.Column(
        db.String(200),
        nullable=True,
    )
    price = db.Column(db.Float)
    name = db.Column(
        db.String,
    )
    description = db.Column(
        db.Text(300),
    )
    quantity = db.Column(
        db.Integer,
        default=0,
    )
    catergory = db.Column(
        db.Enum(ProductCategory),
    )
    is_visible = db.Column(db.Boolean(True))
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.now,
    )
