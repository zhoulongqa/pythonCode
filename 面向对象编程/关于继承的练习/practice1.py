#encoding=utf-8
class A(object):
    def __init__(self,name):
        print "a"
        print id(name)
        self.name = name
        print id(self.name)
    def getName(self):
        print self.name
class B(object):
    def __init__(self):
        print "b"
a=A('a')
b=B()
print a
print b
print id(a)
print id(b)