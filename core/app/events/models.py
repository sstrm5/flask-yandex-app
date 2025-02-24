from datetime import datetime
from app.extensions import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    picture = db.Column(
        db.String(200),
        nullable=False,
    )
    text = db.Column(
        db.String(500),
        nullable=False,
    )
    # author = ...
    is_published = db.Column(
        db.Boolean,
        nullable=False,
        default=True,
    )
