# demaria
# 时间:2023/5/6 16:39

"""
方法名称：
index() 查找str子串第一次出现的位置，若不存在则抛异常ValueError
rindex() 查找str子串最后一次出现的位置，若不存在则抛异常ValueError
find() 查找str子串第一次出现的位置，若不存在则返回-1
rfind() 查找str子串最后一次出现的位置，若不存在则返回-1
"""

s='hello,hello'#长度11
print(s.index('lo')) #3
print(s.find('lo'))#3
print(s.rindex('lo'))
print(s.rfind('lo'))
"""字符长度索引亦可以有正向和逆向，正向从0开始，逆向从-1开始"""

# print(s.index('k'))  #抛异常
print(s.find('k'))