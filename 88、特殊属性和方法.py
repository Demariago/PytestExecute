# demaria
# 时间:2023/5/24 16:08


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


class Person(object):
    def __new__(cls, *args, **kwargs):  # 创建对象
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))  # 4864
        obj = super().__new__(cls)
        print('创建的对象的id为：{0}'.format(id(obj)))  # 7264
        return obj

    def __init__(self, name, age):  # 对创建的对象初始化
        self.name = name
        self.age = age
        print(' _init__被调用了，self的id为：{0}'.format(id(self)))  # 7264


print('object id:{0}'.format(id(object)))  # 4048
print('Person id:{0}'.format(id(Person)))  # 4864
p1 = Person('三', 20)
print('p1 id:{0}'.format(id(p1)))  # 7264

# object id:140709592514048
# Person id:2701662344864
# __new__被调用执行了，cls的id值为2701662344864
# 创建的对象的id为：2701663637264
#  _init__被调用了，self的id为：2701663637264
# p1 id:2701663637264


