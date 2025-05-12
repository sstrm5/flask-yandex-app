import pathlib
from flask import Blueprint, send_from_directory
from core.routes.users.routes import users_bp
from core.routes.news.routes import news_bp

# Blueprint configuration
api = Blueprint("api", __name__)


@api.route("/hello")
def handle():
    return "Привет"


api.register_blueprint(users_bp)
api.register_blueprint(news_bp)


@api.get("/media/<path:path>")
def send_media(path):
    """
    :param path: a path like "posts/<int:post_id>/<filename>"
    """

    return send_from_directory(directory=pathlib.Path("../../media"), path=path)
