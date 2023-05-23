# demaria
# 时间:2023/5/15 20:33

"""
try...except....else结构
解释：try模块中不抛出异常时执行else模块，try模块中抛出异常时执行except模块
"""
try:
    a = int(input('请输入第一个整数'))
    b = int(input('请输入第二个整数'))
    result = a / b
except BaseException as e:
    print('出错了,错误为：', e)
else:
    print('结果为：', result)
print('程序结束')

# 请输入第一个整数a
# 出错了,错误为： invalid literal for int() with base 10: 'a'
# 程序结束

# 请输入第一个整数10
# 请输入第二个整数0
# 出错了,错误为： division by zero
# 程序结束