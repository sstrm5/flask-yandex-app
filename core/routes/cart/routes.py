from flask import Blueprint, render_template
from flask_login import current_user, login_required
from core.app.cart.models import Cart, CartLine
from core.app.extensions import db
from core.app.products.models import Product


cart_bp = Blueprint("cart", __name__)


@login_required
@cart_bp.route("/cart/", methods=["GET"])
def get_cart():
    query = db.session.query(Cart).filter(Cart.user_id == current_user.id).all()
    if query:
        cart = query[0]
    else:
        cart = Cart()
        cart.user = current_user
        db.session.add(cart)
        db.session.commit()
    return render_template("cart/cart.html", cart=cart)


@login_required
@cart_bp.route("/cart/add/<int:product_id>", methods=["GET", "POST"])
def add_product(product_id: int):
    product = db.session.query(Product).get(product_id)
    query = db.session.query(Cart).filter(Cart.user_id == current_user.id).all()
    if query:
        cart = query[0]
    else:
        cart = Cart()
        cart.user = current_user
        db.session.add(cart)
        db.session.commit()
    if not any([product_id == line.product_id for line in cart.lines]):
        cart_line = CartLine()
        cart_line.cart = cart
        cart_line.cart_id = cart.id
        cart_line.product = product
        cart_line.product_id = product.id
        cart_line.quantity += 1
        cart.lines.append(cart_line)
        db.session.add(cart_line)
        db.session.add(cart)
        db.session.commit()
    for line in cart.lines:
        if line.product_id == product_id:
            if line.quantity < product.quantity:
                line.quantity += 1
            db.session.add(line)
            db.session.commit()

    return render_template("cart/cart.html", cart=cart)


@login_required
@cart_bp.route("/cart/remove/<int:product_id>", methods=["GET", "POST"])
def remove_product(product_id: int):
    product = db.session.query(Product).get(product_id)
    query = db.session.query(Cart).filter(Cart.user_id == current_user.id).all()
    if query:
        cart = query[0]
    else:
        cart = Cart()
        cart.user = current_user
        db.session.add(cart)
        db.session.commit()
    if not any([product_id == line.product_id for line in cart.lines]):
        cart_line = CartLine()
        cart_line.cart = cart
        cart_line.cart_id = cart.id
        cart_line.product = product
        cart_line.product_id = product.id
        cart_line.quantity += 1
        cart.lines.append(cart_line)
        db.session.add(cart_line)
        db.session.add(cart)
        db.session.commit()
    for line in cart.lines:
        if line.product_id == product_id:
            if line.quantity > 0:
                line.quantity -= 1
            db.session.add(line)
            db.session.commit()

    return render_template("cart/cart.html", cart=cart)
