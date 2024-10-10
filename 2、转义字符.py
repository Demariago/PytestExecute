# demaria
# 时间:2023/4/20 16:19
#反斜杠的使用

#\n换行  newline
print('hello\nworld')
#\t增加四个空格的位置  tab
print('hello\tworld')
print('helloooo\tworld')#解释制表符的含义,每四个
print('he\tworld')
#r  return回车 将光标定位到该行初始位置
print('hello\rwo')
#\b  退一个格的含义 back
print('hello\bworld')
#想要输出单引号呢，用反斜杠标记为正常内容，非边界
print('老师说:\'大家好\'')

#原字符，不希望转义生效，加R或者r，注意最后一个字符不能是反斜杠；可以是两个反斜杠
print(r'hello\nworld')
print(r'hello\nworld\\')



