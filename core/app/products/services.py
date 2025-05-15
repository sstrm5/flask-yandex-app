from dataclasses import dataclass
from abc import ABC, abstractmethod
from core.app.extensions import db
from core.app.products.models import Product


class IProductService(ABC):
    @abstractmethod
    def get_visible_product_list(page: str | None, sorting: str | None): ...
    @abstractmethod
    def get_all_products(): ...
    @abstractmethod
    def change_product_visibilty(id: int): ...
    @abstractmethod
    def edit_product_item(
        id: int,
        name: str,
        description: str,
        price: int,
        picture1: str,
        picture2: str,
        picture3: str,
        is_visible: bool,
    ): ...
    @abstractmethod
    def get_product_item(id: int): ...
    @abstractmethod
    def delete_product_item(id: int): ...
    @abstractmethod
    def create_product_item(
        id: int,
        name: str,
        description: str,
        price: int,
        picture1: str,
        picture2: str,
        picture3: str,
        is_visible: bool,
    ): ...


class ProductService(IProductService):
    def get_visible_product_list(page: str | None, sorting: str | None):
        page = int(page) if page else 1
        sorting = sorting if sorting else "default"

        query = db.session.query(Product).filter(Product.is_visible == True)

        # TODO: фильтрация
        # if category:
        #     query = query.filter(Product.category == category)

        product_list = query.all()

        products_quantity = len(product_list)

        return product_list[(page - 1) * 4 : page * 4], products_quantity
