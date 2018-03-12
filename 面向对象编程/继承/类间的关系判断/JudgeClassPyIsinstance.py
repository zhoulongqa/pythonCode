#encoding=utf-8
'''
如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回True，否则返回False
'''
class UniversityMember(object):
    pass
class Student(UniversityMember):
    pass

vm=UniversityMember()   #创建父类的实例
s=Student()             #创建子类的实例

if isinstance(vm,UniversityMember):
    print u"vm是UniversityMember类或其子类的实例对象"
else:
    print u"vm不是UniversityMember类或其子类的实例对象"

if isinstance(s,UniversityMember):
    print u"s是UniversityMember类或其子类的实例对象"
else:
    print u"s不是UniversityMember类或其子类的实例对象"