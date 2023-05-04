# demaria
# 时间:2023/5/4 14:45

"""
列表增加元素的方法
append()，在列表末尾增加一个元素
extend(),在列表末尾至少增加一个元素
insert()，在列表任意位置增加一个元素
切片,在列表任意位置增加至少一个元素
"""

lst=[10,20,30]
print(lst,id(lst))
lst.append(100)
print(lst,id(lst))#注意：id是不变的

lst2=['hello','world']
#lst.append(lst2)
#print(lst)#这种方式将lst2作为一个元素加到末尾

lst.extend(lst2)
print(lst)#将lst2的元素，分别添加到lst的末尾；用来列表拼接


lst.insert(1,90)#索引为1的位置上增加90
print(lst)

lst3=[True,False,'hello']
lst[1:]=lst3#注意：切掉的部分用新列表替换
print(lst)