#encoding=utf-8
'''
类方法：
类方法是类对象所拥有的方法，在类的内部使用关键字def定义的方法，但与一般方法不同的是，需要用修饰器"@classmethod"来标识其为类方法，并且在定义类方法时需要把类本身的实例(cls,指向该类本身)作为参数传进入
类方法既可以直接使用类名去调用，也可以使用类的实例去调
'''
class Person(object):
    id=12   #类静态成员在这定义
    def __init__(self,name):
        self.name=name
        self._inName='ads'
    @classmethod    #类方法定义，用注解方式说明
    def up(cls,a):  #这是cls，而不是self
        print cls,cls.__name__
        return a+1
#创建类的实例
p=Person('alpha')
#调用类方法
print Person.up(20) #类名直接调用
print p.up(12)  #通过实例对象调用