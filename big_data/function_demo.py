"""
 装饰器
"""


def repeat(number=3):
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result

        return wrapper

    return actual_decorator


@repeat(2)
def foo():
    print("foo")


@repeat()
def foo1():
    print("foo1")


if __name__ == '__main__':
    print('------')
    foo()
    foo1()
