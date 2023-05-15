# demaria
# 时间:2023/5/8 14:40
"""
在函数调用过程中，进行参数的传递，如果是不可变对象，在函数体内的修改不会影响实参的值！！！

如果是可变对象，修改形参影响实参

不可变对象 : Number,String,Tuple,bool

可变对象 ： List，Set，Dictionary
"""
def fun(arg1, arg2):
    print('arg1=', arg1)
    print('arg2=', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1=', arg1)
    print('arg2=', arg2)


n1 = 11
n2 = [22, 33, 44]
print('n1=', n1)
print('n2=', n2)
print('+++++++++++++')
fun(n1, n2)
print('n1=', n1)
print('n2=', n2)





# n1= 11
# n2= [22, 33, 44]
# +++++++++++++
# arg1= 11
# arg2= [22, 33, 44]
# arg1= 100
# arg2= [22, 33, 44, 10]
# n1= 11
# n2= [22, 33, 44, 10]