# demaria
# 时间:2023/5/5 10:24

"""
获取字典视图
keys() 获取字典中所有key
values() 获取字典中所有value
items() 获取字典中所有key,alue对
"""

scores={'张三':100,'李四':200,'王五':300}
keys=scores.keys()
print(keys,type(keys))
print(list(keys),type(list(keys)))#进行dict的所有键list类型转换

values=scores.values()
print(values,type(values))
print(list(values),type(list(values)))#将所有value进行转换为list类型

items=scores.items()
print(items)
print(list(items))#转换之后的是由元组组成的



"""
字典元素的遍历
"""
#获取的是字典中的键
print('==========================')
for item in scores:
    print(item)
#获取字典中的values呢
    print(scores[item])
#key和value一一对应打印呢？
    print(item,'分值是：',scores[item])