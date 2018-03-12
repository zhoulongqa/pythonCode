#encoding=utf-8
class animals(object):
    name='bird'
    def __init__(self,name):
        self.name=name

    @classmethod
    def getName(cls):
        return cls.name

    def get_name(self):
        return self.name
a=animals("dog")
print a.getName()
print a.get_name()
print "------------------------"
print animals.getName()
