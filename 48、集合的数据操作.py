# demaria
# 时间:2023/5/5 19:42

"""
交集的含义 A∩B intersection 或者使用 ＆
并集的含义 A∪B union 或者使用 |
差集的定义 A-A∩B diffence 或者使用 - 减号
对称差集定义 A∪B-A∩B symmetric_difference 或者 ^ 符号
"""

s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))#取s1和s2的交集
print(s1 & s2)#或者用&取交集

print(s1.union(s2))#去掉重复元素后二者并集
print(s1|s2)#或者用|

print(s1.difference(s2))#s1-s1∩s2，差集
print(s1-s2)#等同于diffence

print(s1.symmetric_difference(s2))#对称差集
print(s1^s2)
