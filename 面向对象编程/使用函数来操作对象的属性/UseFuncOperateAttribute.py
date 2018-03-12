#encoding=utf-8
'''
使用函数来操作对象的属性：
1、getattr(obj,name[,default])：访问对象的属性，如果存在返回对象属性的值，否则抛出AttributeError异常
2、hasattr(obj,name):检查是否存在某个属性，存在返回true，否则返回false
3、setattr(obj,name,value):设置一个属性，如果属性不存在，会创建一个新属性，该函数无返回值，若存在则更新这个值
4、delattr(obj,name)：删除属性，如果属性不存在则抛出AttributeError异常，该函数也无返回值
'''
class Employee(object):
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print "total employee:",Employee.empCount

    def displayEmployee(self):
        print "name:",self.name,",salary:",self.salary

#创建Employee的实例对象
emp1=Employee("王泽亮",'10000')

if hasattr(emp1,'name'):
    print u"属性name存在"
else:
    print u"属性name不存在"


#访问对象的属性
try:
    a=getattr(emp1,'name')      #返回name属性的值
    print u"name属性的值：",a
except Exception,e:
    print e

#给实例添加一个属性
setattr(emp1,'tel','13381208509')   #添加tel属性
try:
    a=getattr(emp1,'tel')   #返回tel属性的值
    print u"新添加的tel属性的值：",a
except Exception,e:
    print e

#删除某个属性
try:
    delattr(emp1,'tel') #删除tel属性
except Exception,e:
    print e
else:
    #未发生异常时执行这里
    if hasattr(emp1,'tel'):     #如果存在tel属性，返回True，否则返回False
        print u"属性tel存在"
    else:
        print u"属性tel不存在"