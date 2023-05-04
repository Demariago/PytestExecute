# demaria
# 时间:2023/4/28 21:01


# 和if 搭配；和while 搭配；和for 搭配
# 对于while 和for 而言，没有执行break的语句的情况下，执行完循环次数后，会执行else语句

for item in range(3):
     pwd=int(input('请输入密码:'))
     if pwd==888:
         print('密码正确')
         break
     else:
         print('密码不正确')
else:#这个else的使用
    print('三次机会用完，密码不正确')
