#encoding=utf-8
'''
在python中，运算符重写的方式很简单，每个类都会有默认内置的一些运算符方法，
只要重写这个方法，就可以实现针对该运算符的重写
'''
class Vector(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "Vector(%d,%d)" % (self.a,self.b)
    def __add__(self,other):
        return Vector(self.a+other.a,self.b+other.b)

x=Vector(3,7)
y=Vector(1,-10)
print x+y
print str(x)