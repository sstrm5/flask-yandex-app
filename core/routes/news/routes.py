from flask import Blueprint, redirect, render_template, Response, request
import flask_login

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
from werkzeug.utils import secure_filename


news_bp = Blueprint("news", __name__)


@news_bp.route("/news/", methods=["GET"])
def get_news():
    page = request.args.get("page")
    news_type = request.args.get("news_type")
    sorting = request.args.get("sorting")
    use_case = GetNewsUseCase(
        news_service=NewsService,
    )
    news, page_quantity = use_case.execute(
        page=page, news_type=news_type, sorting=sorting
    )
    return render_template(
        "news/news.html", news=news, page=page, page_quantity=page_quantity
    )


@news_bp.route("/news/<int:id>", methods=["GET"])
def get_news_item(id: int):
    news_item = NewsService.get_news_item(id)
    return render_template("news/news-item.html", news_item=news_item)


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
    filename = ""
    if request.method == "POST":
        file = request.files["picture"]
        filename = secure_filename(file.filename)
        file.save(f"./media/img/{filename}")
    if form.validate_on_submit():
        use_case.execute(
            id=id,
            title=form.title.data,
            picture=f"media/img/{filename}",
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
    filename = ""
    if request.method == "POST":
        file = request.files["picture"]
        filename = secure_filename(file.filename)
        file.save(f"./media/img/{filename}")
    if form.validate_on_submit():
        use_case.execute(
            title=form.title.data,
            picture=f"media/img/{filename}",
            text=form.text.data,
            author=flask_login.current_user,
            is_published=form.is_published.data,
        )
        return redirect("/news/edit")
    return render_template("news/news-item-add-form.html", form=form, id=id)
