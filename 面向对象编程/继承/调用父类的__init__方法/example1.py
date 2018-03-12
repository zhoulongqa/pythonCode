#encoding=utf-8
class A(object):
    name=''
    def __init__(self):
        self.name="fosterwu"
    def getName(self):
        return "A"+self.name
class C(A):
    def __init__(self):
        super(C,self).__init__()    #调用基类构造方法
if __name__=='__main__':
    c=C()
    print c.getName()