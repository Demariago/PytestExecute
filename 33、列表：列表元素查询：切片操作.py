# demaria
# 时间:2023/5/4 11:38
"""
列表切片操作
语法格式    列表名[start:stop:step]
关键点：
start和stop是左闭右开 [start,stop)
切出来的是新的列表对象
step默认步长为1
step为正数时：切片默认的是开始的是第一个元素，默认的终止是最后一个元素[:stop:step] [stop::step]的用法
step为负数时：切片默认的是开始的是最后一个元素，默认的终止是第一个元素[:stop:step] [stop::step]的用法
注意step正负时元素顺序

"""

lst=[10,20,30,40,50,60,70,80,90]#注意上一章学习的正序索引从0开始的
#start=1 stop=6 step=1
print(lst[1:6:1])
print('原列表:',id(lst))
lst2=lst[1:6:1]
print('新列表:',id(lst2))
print(lst[:3:2])
print(lst[1::3])
print(lst[-1:-6:-2])
print(lst[-2::-3])
print(lst[::-1])#列表倒排了，逆序输出
print(lst[8::-1])#同上面的逆序效果

print(lst[6:0:-2])#注意和下面的不同!!!
print(lst[6::-2])#注意和上面的不同!!!
print(lst[1::])
print(lst[1:])

