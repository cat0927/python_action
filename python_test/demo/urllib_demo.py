import urllib.parse
import urllib.request
import urllib.response

"""
 使用 Python-urllib 进行发送请求
"""
url = "http://www.baidu.com"
data_dict = {"word": "hello word"}

data = bytes(urllib.parse.urlencode(data_dict), encoding="utf-8")

request_obj = urllib.request.Request(url=url, data=data, method="POST")
response_str = urllib.request.urlopen(request_obj)

print(response_str.read.decode("utf-8"))

if __name__ == '__main__':
    print("-------------")

