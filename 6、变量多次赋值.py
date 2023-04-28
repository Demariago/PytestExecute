# demaria
# 时间:2023/4/21 14:16
name='maliya'
print(name,id(name))
name='liyama'
print(name,id(name))
#从内存上解释来说，再次赋值后，初次内存会变为垃圾，会被回收，所以打印的是最后的一个内存空间
