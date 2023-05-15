# demaria
# 时间:2023/5/8 9:10

"""
用比较运算符  > < >= <= != ==
从第一个开始比较，第一个字符相等就比较第二个，直到两个字符串有不相等字符，比较出不相等字符后，就不再往后比较

原理：用ord获取原始值进行比较的；和chr获取原始字符刚好是对应的

"""

print('apple'>'app')#True
print('apple'>'banana')#False

print(ord('a'),ord('b'))
print(chr(97),chr(98))
print(ord('杨'))
print(chr(26472))


"""
再讲一下==和is的区别
==比较的是value
is 比较的是id（内存id地址）
"""

