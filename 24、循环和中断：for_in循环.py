# demaria
# 时间:2023/4/28 9:03

#for in 循环
#in 从字符串或者序列中依次取值，称之为遍历
#for_in的对象必须是可迭代对象
#语法结构
#for 自定义变量 in 可迭代对象:
#    循环体
#
for item in 'python':#第一次取值p赋值给item并打印；第二次取y并赋值给item并打印。。。。。。
    print(item)

#range()可迭代整数序列
for i in range(1,10,2):
    print(i)

#如果在循环体中，不需要使用自定义变量，可将自定义变量写为"_"  下划线
for _ in range(5):
    print('hello')

#使用for循环，计算1-100之间的偶数和
sum=0
for i in range(1,101):
    if i%2==0:
       sum+=i
print(sum)