import pathlib
from flask import Blueprint, redirect, render_template
from flask_login import login_required, login_user, logout_user
from core.app.extensions import db
from core.app.users.forms.user import LoginForm, RegisterForm
from core.app.users.models import User
from core.app import login_manager

users_bp = Blueprint("users", __name__)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@users_bp.route("/")
def index():
    return render_template("index.html")


@users_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@users_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template(
            "login.html", message="Неправильный логин или пароль", form=form
        )
    return render_template("login.html", title="Авторизация", form=form)


@users_bp.route("/register", methods=["GET", "POST"])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template(
                "register.html",
                title="Регистрация",
                form=form,
                message="Пароли не совпадают",
            )
        if db.session.query(User).filter(User.email == form.email.data).first():
            return render_template(
                "register.html",
                title="Регистрация",
                form=form,
                message="Такой пользователь уже есть",
            )
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html", title="Регистрация", form=form)
