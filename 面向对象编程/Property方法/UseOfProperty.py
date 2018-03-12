#encoding=utf-8
'''
通过property方法可以把对象变量(self.Name)的获取、修改和删除方法自动映射到类变量(bob.name)的三种行为
'''
import os
class Person(object):
    def __init__(self,name):
        self.Name=name
    def getName(self):
        print "fetch...."
        return self.Name
    def setName(self,name):
        print "Change..."
        self.Name=name
    def delName(self):
		print "remove..."
		del self.Name
    name=property(getName,setName,delName,'name property docs')

bob=Person('Bob Smith')
print bob.name
bob.name='Robert Smith'
print bob.name
del bob.name