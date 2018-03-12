class A(object):
    count=0
    print 'a'
    def __init__(self):
        A.count+=1
        print "x"
    def getCount(self):
        return A.count
a=A()
b=A()
c=A()
print a.getCount()