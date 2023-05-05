# demaria
# 时间:2023/5/5 16:34


"""
集合查询在不在使用in;not in

集合新增：add()一次增加一个元素
         update()一次至少增加一个元素:可增加列表list，元组set，集合set
"""

#集合相关操作:查询
s={10,20,30,405,'hello',5.7}
print(10 in s)
print(100 not in s)



#集合的添加
s.add(99)
print(s)
s.update([100,200,300])#添加列表
print(s)
s.update({345,456})#添加集合
print(s)
s.update((888,666))#添加元组
print(s)




#集合的删除
s.remove(100)
print(s)

#s.remove(1000)  上报Error，
s.discard(500)
print(s)#无该元素，但是不报错

s.pop()#不可指定参数去删除，随机删除
print(s)

s.clear()#清空集合元素
print(s)