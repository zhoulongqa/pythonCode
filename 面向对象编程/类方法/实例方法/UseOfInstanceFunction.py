#encoding=utf-8
'''
实例方法是类中定义的普通方法，定义时需要传入隐式参数self，且为第一个参数，调用时不需要，
并且只能通过实例调用
'''
class Person(object):
    id=12       #类静态成员在这定义
    def __init__(self,name):
        self.name=name
        self._inName="ads"

    def getName(self):  #实例方法，需要传入self参数
        return self.name
#创建类的实例
p=Person("alpha")
#通过实例对象调用，无法通过类对象调用
print p.getName()
