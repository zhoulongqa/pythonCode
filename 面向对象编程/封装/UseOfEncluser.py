#encoding=utf-8
__metaclass=type    #确定使用新式类
class Animal(object):
    def __init__(self,name):
        #构造方法一个对象建立后会立即调用此方法
        self.name=name
        print self.name

    def accessibleMethod(self):
        #指定方法对外公开
        print "I have a sell current name is"
        print self.name
        print "the secret message is:"
        self.__inaccessible()

    def __inaccessible(self):
        #私有方法对外不公开以双下划线开头
        print U"cannot see me..."

    @staticmethod
    def staticMethod():
        #self.accessibleMethod()在静态方法中无法直接调用实例方法直接抛出
        print "This is a static method"

    def setName(self,name): #访问器函数
        print "setName"
        self.name=name

    def getName(self):      #访问器函数
        print "getName"
        return self.name

a=Animal("learns")
print a.getName()
a.setName="sr"
print a.getName()
'''
a.accessibleMethod()
a.staticMethod()
'''