# demaria
# 时间:2023/4/27 9:48

#在分支结构开始前，先讲讲对象的布尔值
#所有对象都有布尔值（即True和False），使用内置函数bool()；就像id(),type()一样
#以下的bool值都是False
print('-----以下的bool值均为False，其他的对象布尔值均为True')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([]))#空列表
print(bool(list()))#空列表
print(bool(()))#空元组
print(bool(tuple()))#空元组
print(bool(dict()))#空字典
print(bool({}))#空字典
print(bool(set()))#空集合


print('-----其他的对象的布尔值均为True-----')
print(bool(18))
print(bool(True))
print(bool('helloworld'))


#再详细的理解下bool值
print('仔细理解对象的bool值')
age=int(input('输入年龄：'))#当键盘输入为0时，bool判断为False，走的是else的分支
if age:#输入年龄为0时，bool(0)结果是false所以走了else分支，参见line9
    print(age)
else:
    print('年龄为',age)