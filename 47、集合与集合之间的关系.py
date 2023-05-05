# demaria
# 时间:2023/5/5 19:02

"""两个集合是否相等，元素相同就相等"""
s={10,20,30,50}
s2={20,30,50,10}
print(s==s2)#True, 和元素位置无关，无序序列

"""
集合子集

子集 issubset
超集 issuperset
有无交集 isdisjoint(无交集的判断)
"""

s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1))#True,s2是s1的子集
print(s1.issuperset(s2))#True,s1是s2的超集
print(s1.issuperset(s3))#False,不是的，s1没有全包含s3
print(s1.isdisjoint(s3))#s1和s3有交集，所以disjoint是False

