#encoding=utf-8
class test(object):
    def __init__(self,long,height):
        self.long=long
        self.height=height

    @classmethod
    def area_test(cls,long,height):
        return long*height
    @classmethod
    def zhouchang_test(cls,long,height):
        return 2*(long+height)
n=test(100,200)
print n.area_test(100,200)
print n.zhouchang_test(100,200)
print test.area_test(100,200)
print test.zhouchang_test(100,300)