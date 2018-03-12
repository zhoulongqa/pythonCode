#encoding=utf-8
'''
python有一个很有趣的语法，只要定义类型的时候，实现__call__函数，这个类型就称为可
调用的，换句话说，我们可以把这个类型的对象当做函数来使用，相当于重载了括号运算符

该方法用于实例自身的调用
函数原型为：
__call__(self,[,*args[,**kwargs]])
'''
class Next(object):
    List=[]
    name='wu'
    def __init__(self,low,high):
        for Num in range(low,high):
            self.List.append(Num**2)
            self.name="x"
    def __call__(self,Nu):
        return self.List[Nu]
res=Next(1,5)   #res.List = [1,4,9,16]
print res(0)
print res(1)
print res(2)
print Next.List
print Next.name
print res.name