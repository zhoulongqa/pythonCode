
#encoding=utf-8
class student(object):
    def __init__(self,name):
        self._name=name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if len(value)<10:
            self._name=value
        else:
            raise Exception
s=student("fosterwu")
print s.name

try:
    s.name="12345678901"
    print s.name
except Exception:
    print "name set too long"