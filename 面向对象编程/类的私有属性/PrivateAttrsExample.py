#encoding=utf-8
class employee(object):
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def __addSalary(self):
        return self.__salary*2
    def getAddSalary(self):
        return self.__addSalary()
emp1=employee("fosterwu",10000)
print emp1.get_salary()  #10000
print emp1.getAddSalary()  #20000
#print emp1.__salary   #报错，没有属性