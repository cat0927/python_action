"""
  延迟求值属性
"""


class InitOnAccess:
    def __init__(self, klass, *args, **kwargs):
        self.klass = klass
        self.args = args
        self.kwargs = kwargs
        self._initialized = None

    def __get__(self, instance, owner):
        if self._initialized is None:
            print('initialized!')
            self._initialized = self.klass(*self.args, **self.kwargs)
        else:
            print('cached!')
        return self._initialized


class MyClass:
    lazily_initialized = InitOnAccess(list, "argument")


if __name__ == '__main__':
    print('-----------')
    m = MyClass()
    print(m.lazily_initialized)
    print(m.lazily_initialized)

