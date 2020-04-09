import time
# import demo.test_1
from test1.test_1 import new_name

def user_info(name, age, address):
    print("name:", name)
    print("age: ", age)
    print("address:", address)


def x_y_sum(x, y=20):
    rs = x + y
    print("x_y_sum:", rs)


# 一个* 不定长参数
def any_num_sum(*args):
    print("args:", args)
    rs = 0
    if len(args) > 0:
        for arg in args:
            rs += arg
    print("any_num_sum:", rs)


# 两个** 不定长参数
def pay(basic, **kwargs):
    print("pay_tax:", kwargs["tax"])
    print("social:", kwargs["social"])


# 拆包
def pay(basic, **fee_dict):
    print("pay_1", fee_dict)


# 递归函数
def func(num):
    if num > 1:
        return num * func(num - 1)
    else:
        return num


# 匿名函数
sum = lambda x, y: x + y


# 闭包-外部函数
def sum_closure(x):
    def sum_inner(y):
        # 调用外部函数变量X
        return x + y

    # 外部函数的返回是内部函数的引用
    return sum_inner


# 闭包
def counter_closure(base=0):
    cnt_base = [base]

    def counter(step=1):
        cnt_base[0] += step
        return cnt_base[0]

    return counter


# 装饰器
def time_counter(function):
    def counter_inner(*args):
        start_time = time.time()
        print("start_time: ", start_time)
        function(*args)
        end_time = time.time()
        print("end_time: ", end_time)
        print("run times: ", end_time - start_time)
    return counter_inner


@time_counter
def sum_1(x, y):
    time.sleep(1)
    print("{} + {} = {}".format(x, y, x + y))


if __name__ == '__main__':
    print('--------------')
    user_info("张三", 20, "北京")
    x_y_sum(10, 15)
    x_y_sum(10)
    pay(800, tax=100, social=200)
    fee_dict = {"tax": 1000, "social": 150}
    pay(800, **fee_dict)

    result = func(5)
    print("func_result: ", result)
    print("sum:", sum(5, 7))
    result_1 = sum_closure(10)
    print("sum_closure: {}".format(result_1))

    rs2 = result_1(5)
    print("rs2: {}".format(rs2))

    counter = counter_closure()
    print("counter: {}".format(counter()))
    print("counter: {}".format(counter()))
    print("counter: {}".format(counter()))

    sum_1(10, 20)

    new_name()
