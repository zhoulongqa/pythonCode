#encoding=utf-8
class Computer(object):
    number=0
    def __init__(self):         #实例化
        self.name='gloryroad'
        Computer.number+=1
    def __del__(self):          #del方法
        print self.name+"is deleted!"
    def __len__(self):          #对应到len方法
        return Computer.number
c=Computer()
print id(c)
print c.name
print len(c)
del c