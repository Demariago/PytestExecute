# demaria
# 时间:2023/5/5 20:10

"""集合生成式和列表生成式基本一致"""
#集合
s={i*i for i in range(1,10)}
print(s)

#列表
lst=[i*i for i in range(1,10)]
print(lst)

#字典
items=['Fruist','Books','Others']
prices=[96,78,85]
d={ item.upper():price for item,price in zip(items,prices)}#.upper是大写转换
print(d)