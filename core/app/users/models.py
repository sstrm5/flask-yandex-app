import datetime
import enum
import sqlalchemy
from core.app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class UserRole(enum.Enum):
    user = "user"
    admin = "admin"
    moderator = "moderator"


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
        autoincrement=True,
    )
    name = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True,
    )
    email = sqlalchemy.Column(
        sqlalchemy.String,
        index=True,
        unique=True,
        nullable=True,
    )
    role = db.Column(
        sqlalchemy.Enum(UserRole),
        default=UserRole.user,
        nullable=False,
    )
    hashed_password = sqlalchemy.Column(
        sqlalchemy.String,
        nullable=True,
    )
    created_date = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now,
    )

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
