# demaria
# 时间:2023/5/4 19:50

"""
字典元素的获取:
第一种 []，如scores['张三']
第二种 get()，如score.get['张三']
二者区别在于[]方式在key不存在时，会抛出KeyError异常；get()如果无对应key则返回None，可以通过参数设置默认的value，在key不存在
时作为打底数据返回
"""

scores={'张三':100,'李四':200,'王五':300}
print(scores['张三'])
#print(scores['赵六'])   #抛出异常
print(scores.get('张三'))
print(scores.get('赵六'))#输出None
print(scores.get('赵六',99))#健不存在时，返回的默认的value


"""
Key存在字典中的判断：
使用in或者not in，根据返回True与否判断是否该字典中有该健

删除键值对
del scores['张三']

scores.clear()  清空字典
"""
print('张三' in scores)
print('赵六' in scores)
print('赵六' not in scores)

del scores['张三']#删除指定键值对
print(scores)

#scores.clear() 清空字典

scores['麻七']=998#修改和添加都可以这么来
print(scores)

scores['王五']=876#修改value
print(scores)