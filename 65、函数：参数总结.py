# demaria
# 时间:2023/5/15 10:31

def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun(11,22,33)#函数调用时的参数传递，位置传参
lst=[13,44,55]
#  print(fun(lst))  报错

fun(*lst)#函数调用时，将列表中的每个元素都转换为位置实参传入
fun(a=100,c=200,b=99) #函数的调用，关键字实参

dic={'a':100,'b':300,'c':456}
fun(**dic)# 函数调用时，字典想要关键字传参，添加两个*，将每个key:value传入



"""
默认值形参，个数可变的位置形参，个数可变的关键字形参
"""
def fun1(a,b=10):#b是默认值形参
    print('a=',a)
    print('b=',b)
def fun2(*args):#个数可变的位置形参
    print(args)
def fun3 (**args2):#个数可变的关键字形参
    print(args2)

fun1(22,33)
fun2(223,44,6677,666)
fun3(a=22,b=99,c=87,d=37)


def fun4(a,b,*,c,d):# *表示c和d必须用关键字实参进行传递:从*之后的参数传递只能关键字传递
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
#fun4(10,20,30,40)
fun4(a=12,b=33,c=55,d=99)
fun4(12,14,c=99,d=88)

def fun5(a,b=10,*,c,**agrs):
    pass
def fun6(*args,**args1):
    pass
def fun7(a,b=10,*args,**args2):
    pass
