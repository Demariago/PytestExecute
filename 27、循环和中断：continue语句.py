# demaria
# 时间:2023/4/28 20:47

#用于结束当前循环，进入下一次循环，和if一起搭配使用
"""for ... in ...:
     .....
     if ...:
         continue
    ...
"""


""" while ...:
     ...
     if...:
        continue
     ...   
"""


#输出1-50之间的5的倍数
"""for i in range(1,51):
    if i%5==0:
        print(i)
"""
#使用continue语句实现呢？
for i in range(1,51):
    if i%5!=0:
        continue
    else:
        print(i)




