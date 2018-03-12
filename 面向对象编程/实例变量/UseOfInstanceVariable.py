#encoding=utf-8
'''
实例变量是在__init__函数里定义的，相当于java和c++的普通变量，只作用于当前类的实例。
示例变量前面需要加上self关键字，表示执行实例本身
'''
class Person(object):
    id=12       #类静态成员在这定义
    def __init__(self,name):
        self.name=name      #类的实例变量
p=Person('linda')
print p.name        #访问对象的实例变量