# demaria
# 时间:2023/5/11 10:57

def fun(num):
    odd=[]#存储基数
    even=[]#存储偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst=[10,29,34]
print(fun(lst))

""" 
函数的返回值
1、若函数无返回值（函数执行完毕，不需要给调用处返回数据），return可省略
2、函数返回值如果是1个，则返回原类型
3、函数返回值如果是多个，则返回元组类型
"""

def fun1():
    return 'hello'
print(fun1())#原类型输出

def fun2():
    return 'hello','world'
str=fun2()
print(str)#输出元组了