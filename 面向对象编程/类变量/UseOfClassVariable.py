#encoding=utf-8
'''
类变量：
Python中类变量也叫类的静态成员变量或类属性，类变量在整个实例化对象中是公用的。类变量定义在类中且在函数体外，类变量通常不作为实际变量使用，它的值在这个类的所有实例之间共享
类量紧接在类名后面定义，相当于java和c++的static变量
实例‘变量在__init__()函数里定义，相当于java和c++的普通变量
'''
class Parent(object):	#define parent class
    parentAttr=100	#类变量
    def __init__(self):
        self.name="zhangsan"
    print "Calling parent construct"
#parentAttr变量就是一个类变量，name就是一个实例变量

Parent()
print Parent().name

p = Parent()
print p.name