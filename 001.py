import requests

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36' }
url = 'https://www.sogou.com/web'
kw = input('Enter a keyword:')
params = {'query': kw}

r = requests.get(url=url, headers=headers, params=params)
page_text = r.text
with open('sogou.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print('Request URL: ', r.url)
print('Request Type: ', r.request)
print('Response status: ', r.status_code)
print('Over')
