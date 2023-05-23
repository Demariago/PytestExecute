# demaria
# 时间:2023/5/16 10:00


"""
类名：一个单词或者多个单词组成，每个单词首字母要大写，其他小写
实例方法
静态方法
类方法
"""
class Student:#Student就是一个类
#python中一切皆是对象，那Student有id吗，type，value呢？
#print(id(Student),type(Student))是对象
   native_pace='吉林'#直接写在类里的变量称之为类属性，在所有方法之外
   def __init__(self,name,age):
       self.name=name#self.name称之为实例属性，进行了一个赋值操作，将name的值赋给实例属性
       self.age=age
   #实例方法
   def eat(self):#注意和函数的不同(self)必须写！！！！，定义在类里的称之为方法，定义在类之外的称之为函数
       print('学生在吃饭')
   #静态方法
   @staticmethod
   def method():#不允许写self！！！！！
       print('我使用了staticmethod进行修饰，我是静态方法')
   #类方法
   @classmethod
   def cm(cls):#注意cls必须写！！！！
       print('我使用了classmethod进行修饰，我是类方法')
