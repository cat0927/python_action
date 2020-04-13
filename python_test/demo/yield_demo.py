"""
generator 生成函数
"""


# yield
def four():
    x = 0
    while x < 4:
        print("generator x=", x)
        yield x
        x += 1


for item in four():
    print("for:{}".format(item))

print('************************')


# yield from
def sub_gen(x):
    for i in range(x):
        yield i


def gen(y):
    yield from sub_gen(y)


for item in gen(6):
    print("item:{}".format(item))

if __name__ == '__main__':
    print('---------')
