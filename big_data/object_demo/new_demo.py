""""
 __new__() 优于 __init__() 执行
"""


class InstanceCountingClass:
    instance_created = 0

    def __new__(cls, *args, **kwargs):
        print('__new__() classed with', cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instance_created
        cls.instance_created += 1
        return instance

    def __init__(self, attribute):
        print('__init__() called with', self, attribute)
        self.attribute = attribute


if __name__ == '__main__':
    print(InstanceCountingClass('abc'))
    print('-------------------------')
    print(InstanceCountingClass('xyz'))
