import time
import hashlib
import pickle

"""
 缓存
"""
cache = {}


def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(function, args, kw):
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            if (key in cache and not is_obsolete(cache[key], duration)):
                return cache[key]['value']

            # 计算
            result = function(*args, **kw)

            # 保存结果
            cache[key] = {
                'value': result,
                'time': time.time()
            }

            return result
        return __memoize
    return _memoize


@memoize(1)
def _sum(a, b):
    print("---sum")
    return a + b


if __name__ == '__main__':
    print('sum1--', _sum(10, 15))
    print('sum2--', _sum(10, 15))
