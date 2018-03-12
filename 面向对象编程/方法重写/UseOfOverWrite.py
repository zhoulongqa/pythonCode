#encoding=utf-8
class parent(object):
    def mymethod(self):
        print "call Parent"
    def printName(self):
        print "my name is Lily"

class Child(parent):
    def mymethod(self):
        print "call child"
        super(Child,self).mymethod()
c=Child()
c.mymethod()
c.printName()