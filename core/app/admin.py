from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from core.app.extensions import db
from core.app.news.models import News
from core.app.users.models import User


# Ограничение доступа в админке
class AdminOnlyView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("login"))


# Функция для инициализации админки
def init_admin(app):
    admin = Admin(app, name="Админка", template_mode="bootstrap4")
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(News, db.session))
