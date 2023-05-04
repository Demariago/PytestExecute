# demaria
# 时间:2023/4/28 21:37
"""break和continue二重循环的使用"""
"""注意内层执行次数"""
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            break
        print(j)


"""注意内层执行次数"""
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            continue
        print(j,end='\t')
    print()

