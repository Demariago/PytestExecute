# demaria
# 时间:2023/4/21 14:25
#结合5 print(type(name))，可以查看类型
#常见的类型有 ：int整形如99；float浮点型如99.99；布尔类型bool只有True，False两个；字符串类型'我的python'



#int的解释：
###不同的进制类型有不同的标识  默认10进制，2进制以0b开头（参见文件3)，八进制以0o开头，十六进制以0x开头
n1=90
n2=-88
n3=0
print('整形',n1,n2,n3)
print(type(n1),type(n2),type(n3))
n4=0b10101101110
print('二进制',n4)
n5=0x1eaf
print('十六进制',n5)




#浮点类型解释：由整数和小数部分构成
n6=3.14159
print(n6,type(n6))
#注意！浮点数精度存储问题，计算时不准确，如下
n7=1.1
n8=2.2
print('n7+n8=',n7+n8)#精度问题出现了，由于计算机是二进制的存储的
#解决浮点预算精度问题
from decimal import Decimal
print('浮点计算',Decimal(n7)+Decimal(n8))#为什么不是3.3，还是因为计算机二进制存储问题吗？？？？？
print('浮点计算',Decimal('1.1')+Decimal('2.2'))



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

