#myl_003#
#数据输入文件
fb=open('D:/text.txt','a+')#文件不存在就创建，在的话就追加内容
print('helloword',file=fb)
fb.close()
#注意1是盘符要存在，2是使用file=


#不进行换行输出，则加逗号
print('hello','world')
#换行输出呢?
print('hello\nworld')

#print可以输出数字，字符串，运算符(加引号的意思是原样输出)
print(444)
print('string')
print(4+6)
n1='wode'
n2='python'
print(n1,n2)
print("*",end='\t')
print()#自带换行
print(1234)