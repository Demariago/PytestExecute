# demaria
# 时间:2023/5/8 10:42

"""
编码：将字符串转换为二进制bytes
解码：将bytes类型数据转换为字符串类型
"""

s='天涯共此时'
#编码操作
print(s.encode(encoding='GBK'))#GBK编码方式，一个中文占据两个字节
print(s.encode(encoding='UTF-8'))#UTF-8编码方式，一个中文占据三个字节

#解码操作，编码解码二者对应的方式要对应一样
byte=s.encode(encoding='GBK')#编码
print(byte.decode(encoding='GBK'))#解码
