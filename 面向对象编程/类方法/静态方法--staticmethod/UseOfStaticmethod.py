#encoding=utf-8
'''
静态方法：
静态方法是在类内部使用关键字def定义的方法，但与其他方法不同的是，需要用修饰器"@staticmethod"来标识其为静态方法，并且在定义静态方法时不需要传入任何隐式参数
静态方法既可以直接使用类名去调用，还可以使用类的实例去调
'''
class Person(object):
    id=12   #类静态成员在这定义
    def __init__(self,name):
        self.name=name

    @staticmethod   #类静态方法定义，用注解方式说明
    def down(b):    #静态方法不需要self，cls变量
        id=13
        print u"类变量=",id
        return b-1
#创建类的实例
p=Person("alpha")
#调用静态方法
print Person.down(15)   #类名直接调用
print p.down(19)        #通过实例对象调用
