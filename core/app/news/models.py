from datetime import datetime
import enum

import sqlalchemy
from core.app.extensions import db
from core.app.users.models import User


class NewsType(enum.Enum):
    regular = "regular"
    important = "important"
    new = "new"


class News(db.Model):
    __tablename__ = "news"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    picture = db.Column(
        db.String(200),
        nullable=True,
    )
    text = db.Column(
        db.String(500),
        nullable=False,
    )
    author_id = db.Column(db.Integer, db.ForeignKey("users.id", name="author"))
    author = db.relationship(User)
    news_type = db.Column(
        sqlalchemy.Enum(NewsType),
        default=NewsType.regular,
    )
    is_published = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
    )
    created_at = db.Column(db.DateTime, default=datetime.now)
