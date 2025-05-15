from flask import Blueprint, render_template, request

from core.app.products.services import ProductService


products_bp = Blueprint("products", __name__)


@products_bp.route("/products/", methods=["GET"])
def get_visible_products():
    page = request.args.get("page")
    sorting = request.args.get("sorting")
    products, products_quantity = ProductService.get_visible_product_list(page, sorting)
    return render_template(
        "products/products.html", products=products, products_quantity=products_quantity
    )
