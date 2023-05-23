# demaria
# 时间:2023/5/16 10:55
"""
对象的创建又称之为类的实例化

"""

class Student:
   native_pace='吉林'
   def __init__(self,name,age):
       self.name=name
       self.age=age

   def eat(self):
           print('学生在吃饭')

#创建类的对象
stu1=Student('张三',20)#已经开内存空间了
stu1.eat()  #对象名.方法名
print(stu1.name)
print(stu1.age)
Student.eat(stu1)#同第19行代码效果  类名.方法名(类的对象)--实际就是方法定义处的self

