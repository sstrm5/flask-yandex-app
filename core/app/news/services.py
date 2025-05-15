from abc import ABC, abstractmethod

from sqlalchemy import desc
from core.app.extensions import db
from core.app.news.models import News
from core.app.users.models import User


class INewsService(ABC):
    @abstractmethod
    def get_published_news(
        page: str | None, news_type: str | None, sorting: str | None
    ): ...
    @abstractmethod
    def get_all_news(): ...
    @abstractmethod
    def update_status_news(id: int): ...
    @abstractmethod
    def edit_news_item(
        id: int, title: str, text: str, picture: str, is_published: bool
    ): ...
    @abstractmethod
    def get_news_item(id: int): ...
    @abstractmethod
    def delete_news_item(id: int): ...
    @abstractmethod
    def create_news_item(
        title: str, text: str, picture: str, author: User, is_published: bool
    ): ...


class NewsService(INewsService):
    SORTING_TYPES = {
        "new": News.created_at,
        "default": News.title,
    }

    def get_published_news(
        page: str | None, news_type: str | None, sorting: str | None
    ):
        sorting = sorting if sorting else "default"

        query = db.session.query(News).filter(News.is_published == True)

        if news_type:
            query = query.filter(News.news_type == news_type)

        news = query.order_by(desc(NewsService.SORTING_TYPES[sorting])).all()

        news_quantity = len(news)

        return news[(page - 1) * 4 : page * 4], news_quantity

    def get_news_item(id: int):
        news_item = db.session.query(News).get(id)
        return news_item

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
        picture: str,
        text: str,
        is_published: bool,
    ):
        news_item = db.session.query(News).get(id)
        news_item.title = title
        news_item.text = text
        news_item.picture = picture
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
        picture: str,
        author: User,
        text: str,
        is_published: bool,
    ):
        news_item = News()
        news_item.title = title
        news_item.text = text
        news_item.picture = picture
        news_item.author = author
        news_item.is_published = is_published
        db.session.add(news_item)
        db.session.commit()
