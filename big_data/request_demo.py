import requests

"""
 requests 模块
"""

_url = "http://www.baidu.com"

data = {
    "key": "python",
    "page": 10
}
try:
    response = requests.get(_url, params=data)
    if response.status_code == 200:
        print("response:{}".format(response))

    print("response_txt:{}".format(response.text))
except Exception as ex:
    print("error:{}".format(ex))


if __name__ == '__main__':
    print("---------")
