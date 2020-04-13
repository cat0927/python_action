from flask import Flask
# 实例化
app = Flask(__name__)

"""
 Flask 路由
"""


# 定义路由
@app.route('/user/<int:id>')
def index(id):
    print("index:{}".format(id))
    return "Hello World!:"


if __name__ == '__main__':
    app.run(port=1100)
