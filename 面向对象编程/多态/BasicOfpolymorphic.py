#encoding=utf-8
class calculator:
    def count(self,args):
        return 1

calc=calculator()

from random import choice
obj=choice(["hello world",[1,2,3],calc])
print obj
print type(obj)
print obj.count('o')
#不同的对象执行相同的方法得到的不同的结果--多态
