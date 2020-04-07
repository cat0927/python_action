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

if __name__ == '__main__':
    print("-----------")