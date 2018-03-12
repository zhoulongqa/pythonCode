class P(object):
    def __init__(self,name):
        self.name=name
    def __call__(self):
        print self.name
    def __str__(self):
        return "P class:"+self.name
p=P("gloryroad")
p()     #调用实例的__call__()方法
print p     #调用实例的__str__方法