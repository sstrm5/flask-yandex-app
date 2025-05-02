from flask import Blueprint
from core import app

# Blueprint configuration
api = Blueprint("api", __name__)


@api.route("/hello")
def handle():
    return "Привет"


api.register_blueprint(users_bp)
