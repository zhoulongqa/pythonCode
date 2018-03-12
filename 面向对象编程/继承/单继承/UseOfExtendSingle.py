#encoding=utf-8
class Person(object):
    def __init__(self,name,sex,height,weight,married):
        self.name=name
        self.sex=sex
        self.height=height
        self.weight=weight
        self.married=married
    def get_name(self):
        return self.name
    def get_sex(self):
        return self.sex
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_married(self):
        return self.married
class Man(Person):
    def __init__(self,salary):
        Person.__init__(self,u"周杰伦",u"男","177","70","Yes")
        self.salary=salary
    def get_salary(self):
        return self.salary
zhou=Man(20000)
print zhou.get_name()
print zhou.get_married()
print zhou.get_salary()