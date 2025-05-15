from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from core.app.cart.models import Cart, CartLine
from core.app.extensions import db
from core.app.news.models import News
from core.app.products.models import Product
from core.app.users.models import User


# Ограничение доступа в админке
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.value == "admin"

    def can_view(self):
        return current_user.is_authenticated and current_user.role.value == "admin"

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("api.users.login"))


class AdminOnlyView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role.value == "admin"

    def can_view(self):
        return current_user.is_authenticated and current_user.role.value == "admin"

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("api.users.login"))


# Функция для инициализации админки
def init_admin(app):
    admin = Admin(
        app, name="Админка", template_mode="bootstrap4", index_view=AdminOnlyView()
    )
    admin.add_view(MyModelView(User, db.session))
    admin.add_view(MyModelView(News, db.session))
    admin.add_view(MyModelView(Product, db.session))
    admin.add_view(MyModelView(Cart, db.session))
    admin.add_view(MyModelView(CartLine, db.session))
