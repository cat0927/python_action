from flask import Blueprint
"""
 定义新闻模块
"""


# 创建一个Blueprint 对象
new_list = Blueprint('news', __name__)


@new_list.route('/news')
def new():
    return '这是新闻模块'
