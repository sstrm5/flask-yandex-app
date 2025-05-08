from flask import Blueprint, redirect, render_template, Response

from core.app.exceptions import AppException
from core.app.news.forms.news import EditNews
from core.app.news.services import NewsService
from core.app.news.use_cases import (
    CreateNewsItemUseCase,
    DeleteNewsItemUseCase,
    EditNewsItemUseCase,
    GetNewsUseCase,
    GetAllNewsUseCase,
    UpdateStatusNewsUseCase,
)


news_bp = Blueprint("news", __name__)


@news_bp.route("/news/", methods=["GET"])
def get_news():
    use_case = GetNewsUseCase(
        news_service=NewsService,
    )
    news = use_case.execute()
    return render_template("news/news.html", news=news)


@news_bp.route("/news/edit/", methods=["GET"])
def edit_news():
    use_case = GetAllNewsUseCase(
        news_service=NewsService,
    )
    news = use_case.execute()
    return render_template("news/news-edit-page.html", news=news)


@news_bp.route("/news/edit/<int:id>", methods=["GET", "POST"])
def edit_news_item(id: int):
    use_case = EditNewsItemUseCase(
        news_service=NewsService,
    )
    news_item = use_case.get_news_item(id=id)
    form = EditNews(obj=news_item)
    if form.validate_on_submit():
        use_case.execute(
            id=id,
            title=form.title.data,
            # picture=...,
            text=form.text.data,
            is_published=form.is_published.data,
        )
        return redirect("/news/edit")
    return render_template("news/news-item-edit-form.html", form=form, id=id)


@news_bp.route("/news/delete/<int:id>", methods=["GET", "POST"])
def delete_news_item(id: int):
    use_case = DeleteNewsItemUseCase(
        news_service=NewsService,
    )
    try:
        use_case.execute(id=id)
    except AppException:
        return Response("Ошибка приложения", status=500, mimetype="text/plain")
    return redirect("/news/edit")


@news_bp.route("/news/update-status/<int:id>", methods=["GET", "POST"])
def update_status_news(id: int):
    use_case = UpdateStatusNewsUseCase(
        news_service=NewsService,
    )
    try:
        use_case.execute(id=id)
    except AppException:
        return Response("Ошибка приложения", status=500, mimetype="text/plain")
    return Response(status=200, mimetype="text/plain")


@news_bp.route("/news/create", methods=["GET", "POST"])
def create_news_item():
    use_case = CreateNewsItemUseCase(
        news_service=NewsService,
    )
    form = EditNews(is_published=True)
    if form.validate_on_submit():
        use_case.execute(
            title=form.title.data,
            # picture=...,
            text=form.text.data,
            is_published=form.is_published.data,
        )
        return redirect("/news/edit")
    return render_template("news/news-item-edit-form.html", form=form, id=id)
