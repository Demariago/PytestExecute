import requests
import json

url = "http://www.baidu.com"
try:
    response = requests.get(url)
    print("Response text:", response.text)
    print("Status code:", response.status_code)
    print("Headers:", response.headers)
    print("Cookies:", response.cookies)
    print("Encoding:", response.encoding)
    print("Content:", response.content)

    # 只有在确定响应是JSON格式时才调用json()
    # print("JSON:", response.json())

except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except json.decoder.JSONDecodeError as e:
    print(f"JSON解析出错: {e}")

cookies = response.cookies
for key, value in cookies.items():
    print(key, value)

"""
属性/方法	      用途
status_code	       HTTP状态码
text	           响应内容文本
content	           响应内容二进制
json()	           返回 JSON 对象
headers	           响应头
cookies	           Cookies
url	               请求 URL
history	           重定向历史
ok	               请求是否成功
iter_content()	   流式读取大文件
"""

print("=================================")
