"""
正则表达式
"""
import re

str = "python java vue c++"
rs = re.match("python", str)
print("rs:{}".format(rs))
print("rs_group:{}".format(rs.group()))

rs_1 = re.match(".", "abc")
print("rs_1:{}".format(rs_1.group()))

rs_2 = re.match("[Hh]", "hello")
print("rs_2:{}".format(rs_2.group()))


def reg_phone(phone):
    rs = re.match("1[3578]\d{9}$", phone)
    if rs is None:
        return False
    else:
        print("reg_phone:{}".format(rs.group()))
        return True


# 内置函数
pattern = re.compile("\w{4,10}@163\.com$")
rs_3 = re.match(pattern, "python@163.com")
print("rs_3:{}".format(rs_3))

rs_4 = re.search("python", "java python, vue")
print("rs_4:{}".format(rs_4))

if __name__ == '__main__':
    print("-----------")
    print(reg_phone("13612345678"))
    print(reg_phone("13612345678abc"))
    print(reg_phone("15612345678abc"))
