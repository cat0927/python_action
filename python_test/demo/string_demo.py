print(":".join("one"))
print(":".join(["one", "two", "three"]))

str = "hello word python : java"
print(str.split())  # ['hello', 'word', 'python', ':', 'java']
print(str.split(":"))  # ['hello word python ', ' java']

# 宽度为10个字符
format_str = "{0:10} word python".format("hello")
print(format_str)

# 由参数定义宽度
format_str_1 = "{0:{1}} word python".format("hello", 10)
print(format_str_1)


if __name__ == '__main__':
    print("-----------")
