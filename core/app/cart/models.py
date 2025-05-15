from datetime import datetime
from core.app.extensions import db
from core.app.users.models import User


class CartLine(db.Model):
    __tablename__ = "cart_lines"

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)

    cart = db.relationship("Cart", back_populates="lines")
    product = db.relationship("Product")


class Cart(db.Model):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", name="author"))
    user = db.relationship(User, back_populates="cart")
    created_at = db.Column(db.DateTime, default=datetime.now)
    lines = db.relationship(
        "CartLine", back_populates="cart", cascade="all, delete-orphan"
    )
