#encoding=utf-8
'''
使用class语句来创建一个新类，class之后为类的名称，类名后有一括号，括号中为基类()
可以有多个基类，然后以冒号结尾
class ClassName(BaseClass1,BaseClass2...):object
    class suite	#类体
类的帮助信息通过ClassName.__doc__查看
Class_suite由类成员、方法、数据属性组成
'''
class Employee(object):
    #所有员工基类
    empCount=0      #类变量(静态变量)，它的值将在整个类的所有实例之间共享，你可以在内部类或外部类使用Employee.empCount访问

    def __init__(self,name,salary):
        #类的构造函数
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        #类方法
        print "total employee:",Employee.empCount

    def displayEmployee(self):
        print "name:",self.name,'salary:',self.salary
e=Employee(u"王泽亮","3000")
print e.name
print e.salary
print e.displayCount()
print e.displayEmployee()

