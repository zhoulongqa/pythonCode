#encoding=utf-8
class Bird(object):
    category=[]
    typeCount=0
    def __init__(self,name,size,talk):
        Bird.category.append(name)
        Bird.typeCount+=1
        self.name=name
        self.size=size
        self.talk=talk
    def description(self):
        print Bird.category
        print Bird.typeCount
        print "name:",self.name
        print "size:",self.size
        print "talk:",self.talk
B1=Bird(u"鹦鹉",'10',u'能说话')
print B1.description()
B2=Bird(u"喜鹊",'5',u'不能说话')
print B2.description()