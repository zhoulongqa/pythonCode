class A(object):
    def __init__(self,name):
        print 'a'
        print id(name)
        self.name=name
        print id(self.name)
    def printName(self):
        print self.name
        return self.name
class B(A):
    def __init__(self,name):
        self.name=name

b=B("wang")
print b.printName()
b.name='South'
print b.name
