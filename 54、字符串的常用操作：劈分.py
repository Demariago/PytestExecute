# demaria
# 时间:2023/5/7 11:26

"""
split()，从左开始劈分，默认按照空格分切，分切后字符串变为了列表;
可追加sep=‘’ ；‘’中添加分隔符 如 |
可追加用maxsplit指定分劈字符串时的最大分劈次数，进过最大分劈次数后，剩余的子串会单独作为一部分

rsplit(),从右开始劈分；其余同split
"""

s='hello world python'
lst=print(s.split())
s1='hello|world|python'
print(s1.split(sep='|'))

print(s1.split(sep='|',maxsplit=1))

print(s.rsplit())
print(s1.rsplit(sep='|',maxsplit=1))