from dataclasses import dataclass

from core.app.news.services import INewsService
from core.app.users.models import User


@dataclass
class GetNewsUseCase:
    news_service: INewsService

    def execute(self, page: str | None, news_type: str | None, sorting: str | None):
        news = self.news_service.get_published_news(
            page=page, news_type=news_type, sorting=sorting
        )
        return news


@dataclass
class GetAllNewsUseCase:
    news_service: INewsService

    def execute(self):
        news = self.news_service.get_all_news()
        return news


@dataclass
class UpdateStatusNewsUseCase:
    news_service: INewsService

    def execute(self, id: int):
        self.news_service.update_status_news(id=id)


@dataclass
class EditNewsItemUseCase:
    news_service: INewsService

    def execute(
        self,
        id: int,
        title: str,
        picture: str,
        text: str,
        is_published: bool,
    ):
        self.news_service.edit_news_item(
            id=id, title=title, text=text, picture=picture, is_published=is_published
        )

    def get_news_item(self, id: int):
        news_item = self.news_service.get_news_item(id=id)
        return news_item


@dataclass
class DeleteNewsItemUseCase:
    news_service: INewsService

    def execute(self, id: int):
        self.news_service.delete_news_item(id=id)


@dataclass
class CreateNewsItemUseCase:
    news_service: INewsService

    def execute(
        self,
        title: str,
        picture: str,
        author: User,
        text: str,
        is_published: bool,
    ):
        self.news_service.create_news_item(
            title=title,
            text=text,
            picture=picture,
            author=author,
            is_published=is_published,
        )
