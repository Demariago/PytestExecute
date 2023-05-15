# demaria
# 时间:2023/5/15 11:53

"""
定义:在一个函数体内调用了该函数本身，称之为递归
组成：递归调用和递归终止条件
优缺点：简单，但是占用内存大，效率低
"""

def fac(num):#计算阶乘
    if num==1:
        return 1
    else:
        res=num*fac(num-1)
        return res

print(fac(3))