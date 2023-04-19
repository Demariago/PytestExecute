import requests
import json

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
params = {
    # base params
    'interval_id': '100:90',
    'action':'',
    # other params
    'type': '24',  # movie type
    'start': '0',  # start index
    'limit': '5', # quantity limit of movies returned
}
url = 'https://movie.douban.com/j/chart/top_list'

r = requests.get(url=url, headers=headers, params=params)
json_data = r.json()
with open('douban-movie-toplist.json', 'w', encoding='utf-8') as fp:
    json.dump(json_data, fp=fp, ensure_ascii=False)
print('Request URL: ', r.url)
print('Request Type: ', r.request)
print('Response json data: ', json_data)
print('Over')