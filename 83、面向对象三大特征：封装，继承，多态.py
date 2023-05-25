# demaria
# 时间:2023/5/19 20:04

"""
方法重写：子类想输出自己独有的东西

"""

class Person(object):#Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age,end='\t')

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
    def info(self):
            super().info()
            print('学号是',self.stu_no)
class Teacher(Person):
    def __init__(self,name,age,toy):
        super().__init__(name,age)
        self.toy=toy
    def info(self):
        super().info()
        print('教龄',self.toy)

stu=Student('张三',20,1001)
teacher=Teacher('李四',33,10)
stu.info()
teacher.info()