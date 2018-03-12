#encoding=utf-8
'''
Python中的dict对象可以直接序列化为json的{}，但是很多时候，可能用class表示对象，比如定义Employee类，然后
直接去序列化就会报错，原因是类不是一个可以直接序列化的对象，但我们可以使用dumps()函数中的default参数来实现
'''
import json
class Employee(object):
    def __init__(self,name,age,sex,tel):
        self.name=name
        self.age=age
        self.sex=sex
        self.tel=tel
    #将序列化函数定义到类里面
    def obj_json(self,obj_instance):
        return{
            'name':obj_instance.name,
            'age':obj_instance.age,
            'sex':obj_instance.sex,
            'tel':obj_instance.tel
        }
emp=Employee('Lily',24,'female','13381208508')
print json.dumps(emp,default=emp.obj_json)
