# demaria
# 时间:2023/4/28 9:27

"""使用for循环 输出100-999之间的水仙花数（各个位数上的三次方等于该数）
   如：
   153=3*3*3+5*5*5+1*1*1
"""
for i in range(100,999):
    ge=i%10 #各位
    shi=i//10%10 #十位
    bai=i//100 #百位
    #print(ge,shi,bai)
    if i==ge**3+shi**3+bai**3:
        print(i)

