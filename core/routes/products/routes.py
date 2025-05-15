from itertools import product
from flask import Blueprint, render_template, request

from core.app.products.services import ProductService


products_bp = Blueprint("products", __name__)


@products_bp.route("/products/", methods=["GET"])
def get_visible_products():
    page = request.args.get("page")
    sorting = request.args.get("sorting")

    products, page_quantity = ProductService.get_visible_product_list(page, sorting)
    page = abs(int(page)) if page else 1

    return render_template(
        "products/products.html",
        products=products,
        page_quantity=page_quantity,
        page=page,
        sorting=sorting,
    )


@products_bp.route("/products/<int:id>", methods=["GET"])
def get_product_item(id: int):
    product = ProductService.get_product_item(id=id)
    return render_template(
        "products/product-item.html",
        product=product,
    )
