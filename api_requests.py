import requests

# 精简后的请求头
headers = {
  "Host": "test.zhongautohealth.com",
  "client-type": "IOS",
  "Accept": "*/*",
  "app-version": "1.0.0",
  "device-id": "4E305308-538F-452D-9193-D677F627C7D0",
  "device-Info": "iPhone SE (3rd generation)) 18.3.1 false",
  "Accept-Language": "zh-Hans-CN;q=1.0, en-CN;q=0.9",
  "Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
  "token": "ios:7eb6d5e0511e4476bc477d266554b9f7",
  "Content-Type": "application/json",
  "User-Agent": "ZHealth/1.0.0 (com.zhongautohealth.user; build:1; iOS 18.3.1) Alamofire/5.10.2",
  "Connection": "keep-alive",
  "app-build": "1"
}

url = "http://test.zhongautohealth.com/navis-gateway-app/api/user/health/simple/Info"

try:
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    print(resp.json())
except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except ValueError as e:
    print(f"JSON解析错误: {e}")