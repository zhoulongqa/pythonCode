#encoding=utf-8
class Person(object):
    __secretCount=0 #私有属性
    def __init__(self,name):
        self.name=name      #实例属性
        self.__inName="ads" #私有属性

    def visit_private_attribute(self):
        self.__secretCount+=1
        print "__secretCount:",self.__secretCount
        print u"__inName:",self.__inName
p=Person("prel")
p.visit_private_attribute()
print u"在类外直接通过实例访问私有属性"
# print p.__inName