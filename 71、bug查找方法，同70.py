# demaria
# 时间:2023/5/15 16:41

lst = [
    {
    'rating': [9.7, 206287],
    'id': '129052',
    'type': ['剧情', '犯罪'],
    'title': '肖申克的救赎',
    'actors': ['蒂姆.罗宾斯', '摩根.弗里曼']
    },
    {
    'rating': [9.8, 206289],
    'id': '129053',
    'type': ['剧情', '爱情'],
    'title': '霸王别姬',
    'actors': ['张丰毅', '张国荣']
    }
    ]
#print(lst)
for item in lst:
    #print(item)#字典类型，两个字典
    for keys in item:
        #print(keys) #打印所有的字典的key的值
       print(keys,'数值是',item[keys])#item[keys]是字典的value的值







