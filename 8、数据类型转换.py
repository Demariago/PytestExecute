# demaria
# 时间:2023/4/21 16:13
#数据类型：整形，浮点型，布尔型，字符串
#数据类型转换是为了将数据进行拼接

#int转换
name='张三'
age=20
print('我的名字是'+name+',今年我'+str(age)+'岁了')#将age的整形转换为字符串  int通过str转换为string类型
#错误的写法 print('我的名字是'+name+',今年我'+age+'岁了')


#转换函数共有   str()  int()  float() 三种
#注意int()转换  文字和小数类字符串无法转化为整数；浮点数转换为整数，抹零取整
#注意float()转换  文字类无法转换，整数转换的话，末尾为.0

#int转换
s1 = '128'
f1 = 98.7
s2 = '67.77'
ff = True
s3 = 'hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))  #字符串为整数串时可以转换
print(int(f1),type(int(f1)))  #为浮点数时，保留整数部分
#print(int(s2),type(int(s2)))  #字符串为浮点数串时，不能转换，会报错
print(int(ff),type(int(ff)))  #转换为1
#print(int(s3),type(int(s3)))  #字符串必须为整数串才可转换，非数字串是不允许转换的


#float转换
s1 = '128.77'
s2 = '77'
ff = True
s3 = 'hello'
i = 802
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),type(float(s3)))  #字符串为非数字串无法转换
print(float(i),type(float(i)))

