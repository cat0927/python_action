"""
面向对象编程
"""


class Animal:

    def eat(self):
        print("正在啃骨头...")

    def drink(self):
        print("正在喝水...")

    def run(self):
        print("正在奔跑...")


# 继承 Animal 类
class Dog(Animal):
    def __init__(self, name):
        print("初始化....")
        self.name = name
        self.__age = 1  # 私有属性

    # 设置私有方法
    def __set_age(self, age):
        self.__age = age

    def set_info(self, name, age):
        if name != "":
            self.name = name
        if age > 0:
            self.__set_age(age)

    # 静态方法
    @staticmethod
    def get_total():
        print("staticmethod.....")


    # 类方法
    @classmethod
    def total_all(dog):
        print("total_all.....")


    def get_info(self):
        print("姓名:{},年龄:{}".format(self.name, self.__age))


if __name__ == '__main__':
    dog = Dog("小狗")
    dog.drink()
    dog.get_info()
    dog.set_info("小黄狗", 10)
    dog.get_info()
    dog.eat()
    dog.run()
    dog.get_total()
    dog.total_all()
