import pathlib
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from .extensions import db
import os

from sqlalchemy import text

from .news.admin import init_admin


# Инициализация базы данных
migrate = Migrate()

login_manager = LoginManager()


def create_app():
    app = Flask(
        __name__,
        template_folder=pathlib.Path("../../templates"),
        static_folder=pathlib.Path("../../static"),
    )
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    conn_str = f"sqlite:///database.db?check_same_thread=False"
    app.config["SQLALCHEMY_DATABASE_URI"] = conn_str
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)

    init_admin(app)

    # Регистрация Blueprint'ов
    from core.api.routes import api

    app.register_blueprint(api)

    try:
        with app.app_context():
            db.session.execute(text("SELECT 1"))
        print("Подключение к sqlite успешно!")
    except Exception as e:
        print(f"Ошибка подключения: {e}")

    with app.app_context():
        db.create_all()

    return app
