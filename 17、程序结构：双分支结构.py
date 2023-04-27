# demaria
# 时间:2023/4/27 10:33
# 双分支结构

# if 条件表达式:
#       执行体1
# else:
#       执行体2

print('-----键盘输入整数，程序判断是奇数还是偶数-----')
s=int(input('请输入数字:'))
if s%2==0:
   print(s,'是偶数')
else:
   print(s,'是奇数')
#上述用到了input函数，int数据类型转换，if语句，bool值判断