from flask import Flask
from flask_migrate import Migrate
from app.extensions import db
import os

from sqlalchemy import text

from app.events.admin import init_admin


# Инициализация базы данных
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    POSTGRES_USER = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_HOST = os.getenv('POSTGRES_HOST')
    POSTGRES_PORT = os.getenv('POSTGRES_PORT')
    POSTGRES_DB = os.getenv('POSTGRES_DB')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    init_admin(app)

    # Регистрация Blueprint'ов
    from api.routes import api
    app.register_blueprint(api)

    try:
        with app.app_context():
            db.session.execute(text('SELECT 1'))
        print("Подключение к PostgreSQL успешно!")
    except Exception as e:
        print(f"Ошибка подключения: {e}")

    with app.app_context():
        db.create_all()

    return app
