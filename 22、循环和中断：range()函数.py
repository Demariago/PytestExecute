# demaria
# 时间:2023/4/27 20:46

#range的三种创建方式;range用于生成一个整数序列    range(start,stop.step)

#第一种，括号里只有一个数值
r=range(10)#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]；默认从0开始，步长为1
print(r)
print(list(r))#查看range的整数序列---list是列表的意思

#第二种，括号里给了两个值（给出了开始和结束）
r=range(1,10)#从1开始，到10结束，但是不包含10，默认步长为1
print(list(r))

#第三种，括号里会给三个参数，开始&结束&步长
r=range(1,10,2) #注意：左闭右开区间
print(list(r))

#判断10是否在序列中
print('10在不在序列中',10 in r)
print('9在序列中',9 in r)

#range优点：range存储空间和list序列有多长无关，只存储start，stop，step，内存是一样的；只有在使用range对象时才计算相关元素