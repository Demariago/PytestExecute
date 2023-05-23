# demaria
# 时间:2023/5/17 16:14
"""
面向对象的三大特征
1、封装:提高程序的安全性
将数据(属性)和行为 (方法) 包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。
这样，无需关心方法内部的具体实现细节，从而隔离了复杂度。
在Python中没有专门的修饰符用于属性的私有如果该属性不希望在类对象外部被访问，前边使用两个“”

2、继承：提高代码的复用性继承:

3、多态：提高程序的可扩展性和可维护性多态:
"""
"""封装"""
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#年龄不希望在类的外部被使用
    def show(self):
        print(self.name,self,age)

stu=Student('张三',15)
#stu.show()   会报错
print(stu.name)
print(dir(stu))#查询可调用的方法或者类属性
print(stu._Student__age)#在类的外部，通过_Student__age进行访问不希望被调用的类属性，不建议这种访问方式
