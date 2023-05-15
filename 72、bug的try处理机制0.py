# demaria
# 时间:2023/5/15 20:07

"""
被动掉坑：逻辑无错，但是用户错误操作或者例外导致报错

异常处理机制：增加try机制,配合except捕获异常
若是捕获所有可能得异常，需要多个except配合，按照先子后父的顺序进行；最后增加BaseException


"""

"""
输入两个整数并进行除法运算#这种except 只是捕获了一种异常，其他的如输入str类型的没有捕获
try:
 a=int(input('输入a的值'))
 b=int(input('输入b的值'))
 print('a除以b的结果是',a/b)
except ZeroDivisionError:
    print('0不能做为被除数')
print('结束程序')
"""

"""输入两个整数并进行除法运算,完美的程序"""

try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a / b
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不能为0！')
except ValueError:
    print('请输入数字串!')
except BaseException as e:
    print(e)
print('程序结束')