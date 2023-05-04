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
#print(lst)#这种方式将lst2作为一个整体元素加到末尾

lst.extend(lst2)
print(lst)#将lst2的元素，分别添加到lst的末尾；用来列表拼接


lst.insert(1,90)#索引为1的位置上增加90
print(lst)

lst3=[True,False,'hello']
lst[1:]=lst3#注意：切掉的部分用新列表替换
print(lst)



"""
列表元素的删除操作
remove()
一次删除一个元素
重复元素只删除第一个
元素不存在报错ValueError

pop()
删除指定索引位置上的元素
指定元素不存在上报ValueError
不指定索引，则删除列表的最有一个元素

切片
切片后会产生新的列表

clear()
清空列表元素

del()
删除列表
"""

lst10=[10,20,30,40,50,60,30]
lst10.remove(30)#重复元素只移除第一个
print(lst10)
#lst10.remove(100)#报错，元素不存在

lst10.pop(1) #移除位置是1的元素
print(lst10)
#lst10.pop(5)# 报错，最大索引是4
lst10.pop() #不指定索引，删除列表最后一个元素
print(lst10)


print('------切片删除，至少删除一个元素，产生新列表------')
new_lst=lst10[1:3]
print(new_lst)

print('-----切片删除，不产生新列表如何写------')
print('原数组',lst10)
lst10[1:3]=[]#把空列表赋值给切出来的元素！！！！！！！！
print(lst10)

lst10.clear()
print(lst10)

#del lst10  #删除数组

#练习
lst4=[12,22,32]
lst5=[666,777,888]
#将lst5的元素在lst4的第二位上插入进来
lst4[1:1:1]=lst5
print(lst4)