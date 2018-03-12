#encoding=utf-8
'''
Employee类首先被employeeToDict函数转换成dict，然后再被序列化为json。
除了上面这种方法，还有一个方法，因为通常class及其实例都会有一个__dict__属性(除非类中添加了__slots__属性)，
它是一个dict类型，存储的是类或类实例中有效的属性
'''
import json
class Employee(object):
    def __init__(self,name,age,sex,tel):
        self.name=name
        self.age=age
        self.sex=sex
        self.tel=tel
emp=Employee('lily',28,'female','15511144790')
print emp.__dict__      #把实例对象中的所有实例变量组装成一个字典
print(json.dumps(emp,default=lambda Employee:Employee.__dict__))
print(json.dumps(emp,default=lambda emp:emp.__dict__))

