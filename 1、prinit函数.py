#数据输入文件
fb=open('D:/text.txt','a+')#文件不存在就创建，在的话就追加内容
print('helloword',file=fb)
fb.close
#注意1是盘符要存在，2是使用file=


#不进行换行输出，则加逗号
print('hello','world')
#换行输出呢?
print('hello\nworld')