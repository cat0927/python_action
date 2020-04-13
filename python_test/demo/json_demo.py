import json

"""
 JSON 模块
"""
user_info_json = {"name": "zhang_san",
                  "age": 20,
                  "isPython": True,
                  "gender": None,
                  "language": ["Java", "Vue"],
                  "study": {"AI": "python", "bigdata": "hadoop"}}
# 转json
json_str = json.dumps(user_info_json)
print("json_str:{}".format(json_str))

# json 转 Python
python_str = json.loads(json_str)
print("python_str:{}".format(python_str))

if __name__ == '__main__':
    print('----------------')