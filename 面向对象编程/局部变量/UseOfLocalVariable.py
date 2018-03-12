#encoding=utf-8
'''
在类的实例方法中定义的变量，叫局部变量，其作用域仅限于其所在的函数内部，执行到
该函数，局部变量生成，函数退出后，局部变量被消亡
'''
class Person(object):
    id=12       #类静态成员在此定义
    def __init__(self,name):
        self.name=name          #类的实例变量
        self.inName='ads'       #类的实例变量
    def getName(self):
        name='lucy' #局部变量
        return self.name,name       #此处返回实例变量name，同时返回局部变量name
p=Person('linda')
print p.name        #访问对象的实例变量
#通过函数访问实例变量和局部变量
res=p.getName()
print res