#encoding=utf-8
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
emp1=Employee("SR",10000)
emp1.displayCount()   #1
emp1.displayEmployee()  # sr 10000
emp1.salary=20000
emp1.name=u"王亮亮"
emp1.displayEmployee()
emp1.age=27
print emp1.age
emp1.sex="男"
print emp1.sex
#删除age属性
del emp1.age
try:
    print emp1.age
except Exception,e:
    print "该属性已经被删除或该属性不存在"





