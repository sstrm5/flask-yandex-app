from abc import ABC, abstractmethod
from core.app.extensions import db
from core.app.news.models import News


class INewsService(ABC):
    @abstractmethod
    def get_published_news(): ...


class NewsService(INewsService):
    def get_published_news():
        news = db.session.query(News).filter(News.is_published == True).all()
        return news
