# demaria
# 时间:2023/4/28 21:10

#用*打印一个三行四列的矩形
for i in  range(1,4):
    for j in range(1,5):
        print('*',end='\t')#注意print('*')是自带换行的。
    else:
        print()#换行
#和下面的代码做个区分：注意else的位置
print('区分的代码注意else的位置')
for i in  range(1,4):
    for j in range(1,5):
        print('*',end='\t')
else:
    print()

#打印一个9*9的直角三角形
print('9*9的直角三角形')
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end='\t')
    print()

#接9*9的三角形，输出99乘法表
print('9*9的直角三角形')
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()