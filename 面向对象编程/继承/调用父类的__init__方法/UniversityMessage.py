#encoding=utf-8
class UniversityMember(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
class Student(UniversityMember):
    def __init__(self,name,age,no,department):
        UniversityMember.__init__(self,name,age)
        self.no=no
        self.department=department
    def getno(self):
        return self.no
    def getDepartment(self):
        return self.department
s=Student("fosterwu",'19','CS','轻化')
print s.name,s.age
s.name="superman"
print s.name
print s.getName()
print s.getAge()
print s.getno()
print s.getDepartment()
