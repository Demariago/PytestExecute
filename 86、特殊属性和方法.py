# demaria
# 时间:2023/5/24 15:09

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


print(dir(object))


# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
#  '__getattribute__', '__gt__', '__hash__','__init__', '__init_subclass__', '__le__',
#  '__lt__', '__ne__', '__new__',  '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__']

class A:
    pass

class B:
    pass

class C(A, B):
    def __init__(self, name):
        self.name = name

x = C('Jack')
print(x.__dict__)  # {'name': 'Jack'}
print(C.__dict__)  # {'__module__': '__main__', '__init__': <function C.__init__ at 0x000001C1EF107700>, '__doc__': None}
print(x.__class__)  # 对象所属的类<class '__main__.C'>
print(C.__bases__)  # 父类类型的元组(<class '__main__.A'>, <class '__main__.B'>)
print(C.__base__)  # 基类元组<class '__main__.A'>
print(C.__mro__)  # 类的层次结构(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(B.__subclasses__())  # 子类列表[<class '__main__.C'>]