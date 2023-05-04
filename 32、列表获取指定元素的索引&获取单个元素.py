# demaria
# 时间:2023/5/4 10:53



"""索引特点"""
lst=list(['hello',111,3.3,'hello'])
print(lst.index('hello'))   #有多个重复的元素，则只获取第一个元素的索引
#print(lst.index('python'))   #列表不存在该元素时，上报ValuError
print(lst.index(111,1,3))   #指定的范围内查找：左闭右开[1,3),查找111整形



"""索引正向和逆向，正向0到N-1，逆向-N到-1；即list[N]和list[-1]是指向同一个元素
查询的索引超出列表范围时会上报  list  index out of range"""


