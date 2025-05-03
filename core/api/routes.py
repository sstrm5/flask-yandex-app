from flask import Blueprint
from core import app
from core.api.users.routes import users_bp
from core.api.news.routes import news_bp

# Blueprint configuration
api = Blueprint("api", __name__)


@api.route("/hello")
def handle():
    return "Привет"


api.register_blueprint(users_bp)
api.register_blueprint(news_bp)
