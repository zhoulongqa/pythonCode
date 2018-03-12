#encoding=utf-8
class Employee(object):
    '''
    python内置类属性
    python内置类属性：
    python有如下内置的类属性：
     __dict__：类的属性(包含一个字典，由类的数据属性组成)
    __doc__：类的文档字符串，也就是类的帮助信息
    __name__：类名
    __modeule__：类定义所在的模块(类的全名是'__main__className',如果类位于一个导入模块mymod中，那么className.__module__等于mymod)
    __base__：类的所有父类(包含了所有父类组成的元组)
    '''
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print "total employee:",Employee.empCount

    def displayEmployee(self):
        print "name:",self.name,",salary:",self.salary
print "Employee.__doc__:",Employee.__doc__
print "Employee.__name__:",Employee.__name__
print "Employee.__module__:",Employee.__module__
print "Employee.__bases__:",Employee.__bases__
print "Employee.__dict__:",Employee.__dict__
