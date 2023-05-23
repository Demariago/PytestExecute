# demaria
# 时间:2023/5/18 11:22
"""
继承
python支持多继承,可以有多个父类
定义子类时，必须在其构造函数中调用父类构造函数
"""

class Person(object):#Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no=stu_no
class Teacher(Person):
    def __init__(self,name,age,toy):
        super().__init__(name,age)
        self.toy=toy

stu=Student('张三',20,1001)
teacher=Teacher('李四',33,10)
person=Person('王五',99)
stu.info()
teacher.info()
person.info()