# demaria
# 时间:2023/5/5 15:21

"""
集合也是python的内置数据结构
和列表，字典一样都是可变类型的序列
集合是没有value的字典，也是hash后存入内存的，所以位置不可指定
集合中元素不允许重复，重复的会过滤掉；且无序
"""

#创建方式1
s={2,3,4,5,5,6,7,7}
print(s,type(s))

#创建方式2
s=set(range(6)) #list转换为set
print(s)
s2=set([1,2,3,4,4])#直接list转换
print(s2)
s3=set((1,2,4,5,5,65))#元组转换，注意序列顺序
print(s3)
s4=set('python')
print(s4)

#定义一个空集合
s5=set()
print(s5,type(s5))
s6={}
print(type(s6))