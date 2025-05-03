from dataclasses import dataclass

from core.app.news.services import INewsService


@dataclass
class GetNewsUseCase:
    news_service: INewsService

    def execute(self):
        news = self.news_service.get_published_news()
        return news
