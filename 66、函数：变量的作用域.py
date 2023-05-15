# demaria
# 时间:2023/5/15 11:45

"""
变量的作用域：
局部变量：函数内定义并使用，只在函数内生效，局部变量使用global声明，则这边来那个就变为全局变量
全局变量：函数体外定义的变量，可作用于函数内外
"""

def fun(a,b):
    c=a+b #c 称之为局部变量，a和b是形参，作用于函数内部
    return c
# print(c)
# print(a)
# 都报错，局部变量超出了作用域


name='老杨'#name的作用域是全局变量
def fun2():
    print(name)
fun2()


def fun3():
    global age#global 声明，则函数内部的变量作用域也是全局的
    age=20
    print(age)
fun3()
print(age)
