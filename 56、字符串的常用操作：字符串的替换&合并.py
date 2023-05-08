# demaria
# 时间:2023/5/7 16:54

"""
replace() 第一个参数指定被替换的字符，第二个字符指定替换字符，第三个参数指定最大替换次数
join() 将列表[]或者元组()中的字符串组成一个字符串
"""

s='hello,python'
print(s.replace('python','java'))
s='hello,pythpon,python,python'
print(s.replace('python','java',2))
s='hellopython'
print(s.replace('python','helelel'))

lst=['hello','java','python']
print('|'.join(lst))
print(''.join(lst))

t=('hello','world')
print('&'.join(t))

print('*'.join('python'))
