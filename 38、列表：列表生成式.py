# demaria
# 时间:2023/5/4 16:54

"""
列表生成的公式
[i*i for i in range(1,10)]
i*i表示列元素的生成式,或者叫表达式
i为自定义变量
range(1,10)为可迭代对象
"""
lst=[i*i for i in range(1,10)]
print(lst)

lst1=[i for i in range(1,10)]
print(lst1)

#生成一个偶数的序列
lst3=[i*2 for i in range(1,6)]
print(lst3)