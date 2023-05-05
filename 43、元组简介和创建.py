# demaria
# 时间:2023/5/5 11:07

"""
元组是python的内置数据结构之一，是一个不可变序列

不可变序列：字符串，元组；没有增删改的操作
可变序列：列表，字典：可对序列进行增删改操作，对象地址不发生改变

外观上列表和元组就是[]和()的区别



"""

#创建方式第一种
t=('python','hello',90)
print(t,type(t))
#内置函数tuple第二种
t2=tuple(('python','hello',90))
print(t2,type(t2))
#注意，元组中只有一个元素时，()和,不可省略,如下
t3=('python')
t4=('python',)
print(t3,t4,type(t3),type(t4))

#空元组的创建和空列表，空字典类似
lst=[]
lst1=list()

dic={}
dict1=dict()

tup=()
tup1=tuple()
print(lst,lst1,dic,dict1,tup,tup1)


