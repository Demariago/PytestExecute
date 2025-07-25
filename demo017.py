import  requests
resp = requests.request('get','http://test.zhongautohealth.com/navis-gateway-app/api/user/health/simple/Info')
print(resp)