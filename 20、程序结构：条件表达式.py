# demaria
# 时间:2023/4/27 16:28

#if else的简写
num_a=int(input('请输入第一个整数'))
num_b=int(input('请输入第二个整数'))
'''if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
'''
#简化上述代码

print('使用条件表达式比较，简化代码')
print( str(num_a)+'大于等于'+str(num_b) if num_a>=num_b else str(num_a)+'小于'+str(num_b))
#条件判断为True，则执行前面的语句；为False则执行后面的语句
