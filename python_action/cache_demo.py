from flask import Flask
from flask_cache import Cache
import time
"""
 Flask-Cache 
"""


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app)


@app.route('/foo')
@cache.cached(timeout=10 * 6)
def foo():
    time.sleep(1)
    return 'hello foo'


if __name__ == '__main__':
    app.run(port=10010)
