from dataclasses import dataclass


@dataclass
class AppException(Exception):
    @property
    def message():
        return "Ошибка приложения"
