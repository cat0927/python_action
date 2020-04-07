"""
 测试Python类型
"""

# 数字类型
num = 1
name = "张三"
age = 23
high = 180.5
new_str = name + "=>" + "Python" + str(3)

# 测试if
#age_input = input("请输入年龄: ")
new_age = int(18)
if new_age < 18:
    print("年龄小于18")
elif new_age == 18:
    print("年龄等于18")
else:
    print("年龄大于18")

# 测试while
n = 1
while n < 10:
    print("while: ", n)
    n += 1

# for 循环
for i in range(1,6):
    print("for 循环", i)


def new_name():
    print("new_name...")

if __name__ == '__main__':
    print(type(num))
    print(name)
    print(new_str)
    print("姓名: %s, 年龄: %d, 身高：%.1f厘米" %(name, age, high))
    print("find: ", name.find("三"))
    print("nameCount: ", name.count("三"))
