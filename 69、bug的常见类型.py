# demaria
# 时间:2023/5/15 15:07

"""
1、粗心导致的 语法错误 如
 age=input('输入年龄')
    if  age>18
    print('注意')# input默认是str类型，18是int类型，二者不可运行比较运算符

2、中文括号

3、自查宝典
 漏写末尾冒号，如if else，while语句或函数定义语句
 缩进错误
 英文符号写成了中文，如逗号，冒号
 字符串拼接时，类型不一致
 没有定义变量变直接引用
 ==和=的混用

4、知识不熟悉产生的bug
 索引越界 IndexError
 lst=[1,22,333]
 print(lst[3])

 append掌握不熟悉
 lst1=[]
 lst1.append['a','b']



"""