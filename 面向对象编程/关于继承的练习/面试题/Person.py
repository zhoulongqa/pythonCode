#encoding=utf-8
class A(object):
    count=0
    print 'a'
    def __init__(self,name):
        A.count+=1
        self.name=name
    def getName(self):
        return self.name

    @classmethod
    def getCount(gloryroad):
        return gloryroad.count

    @staticmethod
    def getClassName():
        return A.__name__
class B(A):
    def __init__(self,name):
        self.name=name
        A.__init__(self,name)
    def getName(self):
        return self.name.upper()
print A.getCount()
a=A("fosterwu")
print u"通过实例调用实例方法：",a.getName()
print u"通过类对象调用类方法：",A.getCount()
print u"通过实例调用类方法：",a.getCount()
print u"类同对象调用静态方法：",A.getClassName()
b=B("wulaoshi")
print b.getName()
print b.getCount()
print b.getClassName()
print b.name