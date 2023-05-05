# demaria
# 时间:2023/5/5 10:45


"""
将两个列表转换拼接为字典
zip打包时以最少元素生成字典

"""
items=['Fruist','Books','Others']
prices=[96,78,85]
d={ item.upper():price for item,price in zip(items,prices)}#.upper是大写转换
print(d)