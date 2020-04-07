# 信息包含 姓名、年龄、身高、体重，是否会Python
info_list = ["张三", 20, 180, 75, True]
print("info_list:", info_list)
del info_list[1]
print("del_info_list", info_list)

info_list.append("北京市朝阳区")

for info in info_list:
    print("info: ", info)

print("--------------元组---------------")
db_info = ("192.168.2.2", 3306, "root", "psd")
print(db_info)
for item in db_info:
    print(item)

print('-------------字典----------------')
user_info_dist = {"name": "张三", "age": 20, "height": 180, "address": "北京市朝阳区"}

print("user_name: ", user_info_dist["name"])
print("age:", user_info_dist.get("age"))
user_info_dist["tel"] = 10086
print(user_info_dist)
del user_info_dist["height"]
print("删除后：", user_info_dist)
for user in user_info_dist.values():
    print("for_user: ", user)

print('-----------------集合---------------')
student_id_set = {123, 234, 345, 456, 567}
print(student_id_set)
print("len: ", len(student_id_set))
student_id_set.add("789")
print("new_set: ", student_id_set)

string_set = set("hello")
print("string_str: ", string_set)

num_set1 = {1, 2, 4, 7}
num_set2 = {2, 5, 8, 9}
print("交集运算: ", num_set1.intersection(num_set2))
print("交集运算_1: ", num_set1 & num_set2)

print("并集运算： ", num_set1.union(num_set2))
print("并集运算_1： ", num_set1 | num_set2)

print("差集： ", num_set1 - num_set2)
print("差集_1： ", num_set1.difference(num_set2))


if __name__ == '__main__':
    print("-----------main---------------")
    print(info_list)
