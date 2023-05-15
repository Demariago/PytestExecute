# demaria
# 时间:2023/5/8 10:03

"""
第一种：
% 占位符:
%s 字符串占位符
%d 或者%i 整数占位符
%f 浮点数占位符


第二种：
{} 按照0或者1这种位置指定赋值


第三种：
直接f-striing
"""


name='张三'
age=20
print('我叫%s，今年%d岁了'%(name,age))#第一种
print('我叫{0}，今年{1}岁了，我真的叫{0}'.format(name,age))#第二种
print('我叫{name}，今年{age}岁了')#python3以上的方式，第三种



"""
涉及数字精度：
宽度%d
小数点%f
"""

print('%d' % 99)
print('%10d' % 99)#10表示宽度
print('0123456789')
print('%f' % 3.1415926)
print('%.3f'%3.1415926)#.3表示小数点后三位
#同时表示宽度和精度呢?
print('%10.3f' % 3.1415926)#总宽度为10，小数点后3位


#其他表示精度，宽度的方法


print('{0}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))#.3表示一共三位数
print('{0:.3f}'.format(3.1415926))#.3f表示三位小数
print('{0:10.3f}'.format(3.1415926))#同时设置宽度和精度
