# demaria
# 时间:2023/5/7 16:03

"""
isidentifier() 判断字符串是不是合法标识符（字母数字下划线）
isspace()判断字符串是不是全部由空白字符组成（空格，换行，制表符）
isalpha() 判断字符串是否全部由字母组成(汉字也算？？？？？是的)
isdecimal() 判断字符串是否全部由十进制数字组成
isnumeric() 判断字符串是否全部由数字组成（汉字/阿拉伯数字/罗马数字都算）
isalnum() 判断字符串是否全部由字母和数字组成


"""

s='hello,python'
print(s.isidentifier())
s='hello2341_python'#字母数字下划线
print(s.isidentifier())
# False
# True
s=' \n \t'
print(s.isspace())
# True
s='dsjfSDLFJ'
print(s.isalpha())
s='dsf3'
print(s.isalpha())
# True
# False
s='238509'
print(s.isdecimal())
s='九02347'
print(s.isdecimal())
# True
# False
s='32840四五十四'
print(s.isnumeric())
# True
s='sdjf324'
print(s.isalnum())
# True
s='张三kkk888'
print(s.isalnum())#True
s='李四'
print(s.isalpha())#True