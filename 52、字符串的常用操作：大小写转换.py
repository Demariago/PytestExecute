# demaria
# 时间:2023/5/6 17:09

"""
方法名称：
upper() 字符串中所有字符转成大写字母
lower() 字符串中所有字符转成小写字母
swapcase() 字符串中所有大写字符转成小写字母，符串中所有小写字符转成大写字母；大小写转换
capitalize() 把第一个字符转换为大写，其余转换为小写
title() 把每个单词第一个字符转换为大写，把每个单词的其他字符转换为小写
"""

s='hello,python'
s1=s.upper()
print(s1,id(s1),id(s))#转换后内存id变了，说明是不可变序列，产生了新的字符串对象
print(s.lower(),id(s.lower()),id(s))#即便都是小写未实际进行转换，但还是生成新对象

s2='hello,Python'
print(s2.swapcase())
print(s2.title())