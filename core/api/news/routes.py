from flask import Blueprint, render_template

from core.app.news.services import NewsService
from core.app.news.use_cases import GetNewsUseCase


news_bp = Blueprint("news", __name__)


@news_bp.route("/news", methods=["GET"])
def get_events():
    use_case = GetNewsUseCase(
        news_service=NewsService,
    )
    news = use_case.execute()
    return render_template("news/news.html", news=news)
