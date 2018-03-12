#encoding=utf-8
class square(object):
    long=5
    def __init__(self,long):
        self.long=long
    @staticmethod
    def get_area(long):
        return long*long

s=square(10)
print square.get_area(4)
print s.get_area(5)