# demaria
# 时间:2023/4/27 14:58
# 多选一去执行，一般解决连续的区间段问题

# if 表达式1:
#    执行1
# elif 表达式2:
#    执行2
# elif 表达式3：
#     执行3
# else:
#     执行4


#举例  学生的成绩
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 E
# 小于0或者大于100 非法输入
print('-----成绩判断-----')
s=int(input('输入成绩:'))
if  90<=s<=100:#或者一般的常用的写法是 :  s>=90 and s<=100
    print('成绩为A')
elif 80<=s<=89:
    print('成绩为B')
elif 70<=s<=79:
    print('成绩为C')
elif 60<=s<=69:
    print('成绩为D')
elif 0<=s<=59:
    print('成绩为E')
else:
    print("非法输入")