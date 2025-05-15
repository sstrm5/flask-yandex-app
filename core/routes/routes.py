import pathlib
from flask import Blueprint, send_from_directory
from core.routes.users.routes import users_bp
from core.routes.news.routes import news_bp
from core.routes.products.routes import products_bp
from core.routes.cart.routes import cart_bp

# Blueprint configuration
api = Blueprint("api", __name__)


@api.route("/hello")
def handle():
    return "Привет"


api.register_blueprint(users_bp)
api.register_blueprint(news_bp)
api.register_blueprint(products_bp)
api.register_blueprint(cart_bp)


@api.get("/media/<path:path>")
def send_media(path):
    """
    :param path: a path like "posts/<int:post_id>/<filename>"
    """

    return send_from_directory(directory=pathlib.Path("../../media"), path=path)
