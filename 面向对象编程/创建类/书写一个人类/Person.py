#encoding=utf-8
class Person(object):
    def __init__(self,height,weight,skin_color):
        self.height=height
        self.weight=weight
        self.skin_color=skin_color
    def description(self):
        print "height:",self.height
        print "weight:",self.weight
        print "skin_color:",self.skin_color
p=Person(177,70,u"黄")
print p.description()
