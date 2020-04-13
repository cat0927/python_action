from flask import Blueprint

"""
 定义产品模块
"""

product_list = Blueprint('products', __name__)


@product_list.route("/products")
def product():
    return "这是产品模块"
