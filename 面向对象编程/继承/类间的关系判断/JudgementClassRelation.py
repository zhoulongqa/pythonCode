#encoding=utf-8
'''
使用issubclass()或者isinstance()方法来检测类之间的关系
'''
class UniversityMember(object):
    pass
class Student(UniversityMember):
    pass

if issubclass(Student,UniversityMember):
    print u"Student类是UniversityMember类的子类"
else:
    print u"Student类不是UniversityMember类的子类"
