# demaria
# 时间:2023/4/22 20:54

#算数运算符
 #标准算数运算符 加+ 减- 乘* 除/ 整除//  （注意和反斜杠的区别哦）
 #取余运算符%
 #幂运算符**
print('-----------算数运算符----------')
print(1+1)
print(2*2)
print(3/2)
print(5//2)#整除是除完后，去尾取整
print(11%2)#余数是1
print(3**4)
print(9/-4)
 #进阶算法（一正一负的整除计算，向下取整）
print(9//2)
print(-9//-2)
print('-9/2的结果是',-9//2)#注意了！！！
 #进阶算法（取余  公式：余数=被除数-除数*商）(商怎么来的，通过/方式计算来的)
print(9%-4)#     9-(-4)*(-3)=9-12=-3  商-3是怎么来的？9除以-4=-2.25，向下取整为-3
print(-9%4)#     -9-4*(-3)=-9+12=3
print(-13%4)#    -13-4*(-4)=-13+16=3
print(10%-3)






#赋值运算符
 #执行顺序从右到左
 #支持链式赋值
print('-----------赋值运算符----------')
a=b=c=20
print(a,type(a),id(a),b,id(b),id(c))#内存id是一个，指向的是同一个内存空间
 #支持参数赋值 += -= /= //= %= *= =
a=20
a+=30#相当于a+30再赋值给a，好好理解！！！
print(a)
a-=10
print(a)
a*=2
print(a,type(a))
a/=4
print('a的值',a,type(a))#除法出现已经是float类型了
a//=2
print(a)#float类型了已经
a%=3
print(a)

 #支持系列解包赋值
a,b,c=10,20,30# 注意左右数量要相等
print(a,b,c,id(a),id(b),id(c))
#a,b,c=10,20 报错
 #系列解包的用法：交换变量值
print('--------------交换变量-------------')
a,b=10,20
print('交换之前',a,b)
a,b=b,a
print('交换之后',a,b)




#比较运算符：对变量或者表达式的结果进行大小真假比较
 #> < >= <= !=
 #== 对象value的比较
 #is,is not 对象id的比较
print('----------比较运算符----------')
a,b=10,20
print('a>b吗？',a>b)#结果是False，布尔类型
print('a<=b吗？',a<=b)#结果是True
print('a>=b吗？',a>=b)#结果是False
print('a不等于b吗？',a!=b)#True

"""一个=是赋值运算符，一个==是比较运算符
一个变量由三部分组成，标识，类型，值
那么==比较的是值还是标识呢？
比较的是value，比较的是值
比较对象的标识是 is"""

i=10
x=10
print(i==x) #True  比较的是10是否=10 value相等
print(i is x,id(i),id(x)) #True  i和x的标识相等(内存标识)
print('i和x的内存id不相等吗？',i is not x) #i和x的标识（内存id）不相等吗?相等的
 #数组的比较如下
lst1=[1,2]
lst2=[1,2]
print(lst1==lst2)#True
print(lst1 is lst2)#False
print(id(lst1),id(lst2))
print(lst1 is not lst2) #True





#布尔运算符: and ,or, not对运算数取反（bool类型取反）,in, not in
print('-----布尔运算符-----')
a,b=1,2
print(a==1 and b==2) # True and True===True
print(a==1 and b==1) # True and False===False
print(a!=1 and b==1) # False and False===False
print(a!=2 or b==2) #True
print(a!=1 or b!=2)#False

f=True
f1=False
print(not f)
print(not f1)

w='helloworld'
print('w' in w)
print('p' in w)
print('w' not in w)