#encoding=utf-8
'''
json串反序列化成类对象或类的实例，使用的是loads()方法中的object_hook参数来实现
'''
import json
class Employee(object):
    def __init__(self,name,age,sex,tel):
        self.name=name
        self.age=age
        self.sex=sex
        self.tel=tel
#emp=Employee('Lily',24,'female','13381208509')
def jsonToClass(adict):
    return Employee(adict['name'],adict['age'],adict['sex'],adict['tel'])
json_str="{'name':'lucy','age':21,'sex':'female','tel':'15577744561'}"
e=json.loads(json_str,object_hook=jsonToClass)
print e
print e.name