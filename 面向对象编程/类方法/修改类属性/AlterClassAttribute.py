#encoding=utf-8
'''
修改类属性的值，有三种方法
1、通过类方法修改
2、通过实例方法修改
3、直接通过类对象修改
'''
class employee(object):
    city="BJ"               #类属性
    def __init__(self,name):
        self.name=name      #实例变量
    #定义类方法
    @classmethod
    def getCity(cls):
        return cls.city
    #定义类方法
    @classmethod
    def setCity(cls,city):
        cls.city=city
    #实例方法
    def set_City(self,city):
        employee.city=city
emp=employee('joy')          #创建类的实例
print emp.getCity()          #通过实例对象引用类方法  'BJ'
print employee.getCity()     #通过类对象引用类方法  'BJ'
print "------------------------------------------------"
emp.setCity("TJ")       #实例对象调用类方法改变类属性的值
print emp.getCity()    #'TJ'
print employee.getCity()   #'TJ'
print "================================================="
employee.setCity("CD")      #调用类方法改变属性的值
print emp.getCity()   #'CD'
print employee.getCity()  #'CD'
print "**************************************************"
emp.set_City("SH")      #调用实例方法改变类属性的值
print emp.getCity()   #'SH'
print employee.getCity()   #'SH'
print "##################################################"
employee.city=20    #直接修改类属性的值
print emp.getCity()   #20
print employee.getCity()  #20


