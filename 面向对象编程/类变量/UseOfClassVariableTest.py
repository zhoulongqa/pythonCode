#encoding=utf-8
class glorytest(object):
    sum=0
    def __init__(self):
        self.sum=101
    def add(self,a,b):
        count=a+b
        return count
g=glorytest()
print g.sum    #101
print glorytest.sum  #0

g.sum=99
print g.sum   #99
print glorytest.sum  #0
print "===================================="
print g.add(10,100)  #110

h=glorytest()
h.sum=999
print h.sum  #999
print h.add(3,6)  #9
'''
1、当访问类实例时，访问某个变量，变量为实例变量，则返回实例变量的值，不会访问同名的类变量
2、当访问类实例时，访问某个变量，变量不是实例变量，则返回类变量的值
3、当访问类实例时，访问某个变量，变量不是实例变量，也不是类变量，报错
4、类变量，可以通过类名访问，也可以通过类实例访问，前提是没有同名的类实例变量
5、实例变量可以访问类变量，类变量不能访问实例变量
'''

