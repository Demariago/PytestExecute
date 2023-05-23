# demaria
# 时间:2023/5/16 19:57

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20)
stu2=Student('李四',33)
stu1.eat()#调用实例方法
print('---为stu2动态绑定性别属性---')
stu2.gender='女'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

