from flask import Flask, url_for

"""
 add_url_rule 注册路由
"""

# 实例化
app = Flask(__name__)


@app.route('/', endpoint='index')
def hello_world():
    return "hello world"


def end_demo():
    print('-----end_demo----')
    return "end_demo"


app.add_url_rule(rule='/index', endpoint='end_demo', view_func=end_demo)

# 定义路由、endpoint
with app.test_request_context():
    # 构建一个虚拟的请求上线文环境
    print(url_for('index'))

if __name__ == '__main__':
    app.run(port=1100)
