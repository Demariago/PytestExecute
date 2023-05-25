# demaria
# 时间:2023/5/24 11:12

"""
简单地说，多态就是“具有多种形态”，
它指的是:即便不知道一个变量所引用的对象到底是什么类型仍然可以通过这个变量调用方法，
在运行过程中根据变量所引用对象的类型动态决定调用哪个对象中的方法。

Dog Cat继承Animal
Person继承Object类
"""

class Animal():
    def eat(self):
        print('动物都吃')
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
class Person():
    def eat(self):
        print('人吃五谷杂粮')


def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Person())