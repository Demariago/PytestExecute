# demaria
# 时间:2023/5/15 15:49
"""
1、善用print打印去看结果，查看一步步的输出是什么:每一步进行打印输出，看是什么数据类型
2、善用#注释一部分代码
"""
lst = [
    {'rating': [9.7, 206287], 'id': '129052', 'type': ['剧情', '犯罪'], 'title': '肖申克的救赎', 'actors': ['蒂姆.罗宾斯', '摩根.弗里曼']}]

name = input('请输入你要查询的演员')
for item in lst:  # 遍历列表：{}  item是一个又一个的字典
    act_lst = item['actors']
    for actor in act_lst:
        if name in actor:
            print(name, '出演了', item['title'])
    # print(act_lst)
    # for movie in item: #遍历字典，得到movie是一个字典中的key
    #     print(movie)
    # actors=movie['actors']
    # if name in actors:
    #     print(name+'出演了'+movie)