from abc import ABC, abstractmethod
from core.app.extensions import db
from core.app.news.models import News


class INewsService(ABC):
    @abstractmethod
    def get_published_news(): ...
    @abstractmethod
    def get_all_news(): ...
    @abstractmethod
    def update_status_news(id: int): ...
    @abstractmethod
    def edit_news_item(id: int, title: str, text: str, is_published: bool): ...
    @abstractmethod
    def get_news_item(id: int): ...
    @abstractmethod
    def delete_news_item(id: int): ...
    @abstractmethod
    def create_news_item(title: str, text: str, is_published: bool): ...


class NewsService(INewsService):
    def get_published_news():
        news = db.session.query(News).filter(News.is_published == True).all()
        return news

    def get_all_news():
        news = db.session.query(News).all()
        return news

    def update_status_news(id: int):
        news_item = db.session.query(News).get(id)
        news_item.is_published = not news_item.is_published
        db.session.add(news_item)
        db.session.commit()

    def edit_news_item(
        id: int,
        title: str,
        # picture: str,
        text: str,
        is_published: bool,
    ):
        news_item = db.session.query(News).get(id)
        news_item.title = title
        news_item.text = text
        news_item.is_published = is_published
        db.session.add(news_item)
        db.session.commit()

    def get_news_item(id: int):
        news_item = db.session.query(News).get(id)
        return news_item

    def delete_news_item(id: int):
        db.session.query(News).filter(News.id == id).delete()
        db.session.commit()

    def create_news_item(
        title: str,
        # picture: str,
        text: str,
        is_published: bool,
    ):
        news_item = News()
        news_item.title = title
        news_item.text = text
        news_item.is_published = is_published
        db.session.add(news_item)
        db.session.commit()
