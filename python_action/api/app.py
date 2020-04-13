from flask import Flask
from python_action.api.news import new_list
from python_action.api.products import product_list

"""
 使用蓝图管理模块
"""

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello my wold'


# 将 news 模块里的蓝图注册到 app
app.register_blueprint(new_list)
app.register_blueprint(product_list)


if __name__ == '__main__':
    app.run(port=10010)
