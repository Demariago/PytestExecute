# demaria
# 时间:2023/5/4 16:08

"""
sort()列表元素升序排列；也可以指定reverse=True执行降序操作,原列表上操作
也可以调用内置函数sorted(),指定reverse=True进行降序操作，原列表不发生改变
区别是原列表是否影响
"""
lst=[20,33,14,88,35,77,56,25,99]
print('排序前',lst,id(lst))
lst.sort(reverse=True)
print('排序后,降序',lst,id(lst))
lst.sort()
print('排序后,升序',lst,id(lst))


print('--------内置函数sorted()操作列表排序,新列表了------')
lst1=[12,33,22,77,34,17]
print(lst1,id(lst1))
new_lst1=sorted(lst1)
print(new_lst1,id(new_lst1))
new_lst2=sorted(lst1,reverse=True)
print(new_lst2,id(new_lst2))
