# demaria
# 时间:2023/4/28 10:12
#break语句 用于结束循环，通常和if一起使用
#通常是非正常跳出循环
"""for ... in ...:
     .....
     if ...:
         break
"""

""" while ...:
     ...
     if...:
        break
"""
#ATM取款，从键盘读取密码，最多读取三次，如果正确就结束循环，密码是888
"""for item in range(3):
     pwd=int(input('请输入密码:'))
     if pwd==888:
         print('密码正确')
         break
     else:
         print('密码不正确')"""

#while循环上述代码实现方式

x=3
i=1
while i<=x:
    pwd = int(input('请输入密码'))
    if pwd==888:
        print('密码正确')
        break
    else:
        print('密码错误')
    i+=1