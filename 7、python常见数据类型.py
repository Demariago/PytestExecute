# demaria
# 时间:2023/4/21 14:25
#结合5 print(type(name))，可以查看类型
#常见的数据类型行 整数类型，浮点数类型，布尔类型，字符串类型
#常见的类型有 ：int整形如99；float浮点型如99.99；布尔类型bool只有True，False两个；字符串类型'我的python'



#int的解释：
###不同的进制类型有不同的标识  默认10进制，2进制以0b开头（参见文件3)，八进制以0o开头，十六进制以0x开头
n1=90
n2=-88
n3=0
print('整形',n1,n2,n3)
print(type(n1),type(n2),type(n3))
n4=0b10101101110
print('二进制,n4=',n4)
n5=0x1eaf
print('十六进制,n5=',n5)




#浮点类型解释：由整数和小数部分构成
n6=3.14159
print(n6,type(n6))
#注意！浮点数精度存储问题，计算时不准确，如下
n7=1.1
n8=2.2
print('n7+n8=',n7+n8)#精度问题出现了，由于计算机是二进制的存储的
#解决浮点预算精度问题
from decimal import Decimal
print('浮点计算',Decimal(n7)+Decimal(n8))
#为什么不是3.3，还是因为计算机二进制存储问题吗？？？？？
#解释下，因为在将浮点数转换为 Decimal 类型时，浮点数本身可能已经存在精度损失了（因为最初是以 float 类型存储的），它只是基于已经有精度损失的浮点数进行后续操作。
print('浮点计算',Decimal('1.1')+Decimal('2.2'))
#这是一种更推荐的使用 Decimal 类的方式，直接将字符串形式的数值传递给 Decimal 类进行初始化。这样做的好处是避免了浮点数先以 float 类型存储带来的精度问题，而是按照字符串中给定的精确数值来进行后续的运算，能够确保运算的高精度，最终会准确地输出 3.3
print('浮点计算',Decimal(str(n7))+Decimal(str(n8)))
#先将浮点转义为字符串



#布尔类型，True为真，False为假，布尔只有这两个值；布尔类型可以转换为整数，True为1，False为0
#转换时不需要转义
print(True+1)
print(False+1)





#字符串类型
#注意：可以使用单引号，双引号，三引号标记
#单引号双引号的字符串必须在一行
#三引号的可以在多行，解释如下代码

str1='人生苦短，我用python'
str2="人生苦短，我用python"
print(str1,type(str1),str2,type(str2))
str3="""人生苦短，
我用python"""
print(str3,type(str3))



