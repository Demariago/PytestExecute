# demaria
# 时间:2023/5/24 15:46

"""
特殊属性
__dict__ 获得类对象或实例对象所绑定的所有属性和方法的字典
__class__对象所属的类
__bases__ 父类元组
__mro__ 类的层次结构
_subclasses__() 获取子类列表
特殊方法
__len_()  通过重写_len_(方法，让内置函数len()的参数可以是自定义类型
__add_()  通过重写_ add_0)方法，可使用自定义对象具有“+”功能
__new__()  用于创建对象
__init__()  对创建的对象进行初始化
"""

a=10
b=12
c=a+b
print(c)
d=a.__add__(b)
print(d)


class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return   len(self.name)
stu1=Student('詹恩')
stu2=Student('2222')
s=stu1+stu2#实现对象的加法（Students类中，编写__add__()方法）
print(s)

print('--------------')

lst=[11,22,33,44]
print(len(lst))
print(lst.__len__())

print(len(stu1))#len改写，输出了stu1的长度




