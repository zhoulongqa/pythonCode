#encoding=utf-8
class house(object):
    def __init__(self,name):
        print "Calling house constructor"
        self.height=100
        self.width=50
    def get_volumn(self):
        return self.height*self.width*100

class car(object):
    def __init__(self):
        print "Calling car constructor"
        self.engine="gasoline type engine"
    def carry_people_bumber(self):
        return 15

class carHouse(house,car):      #多重继承
    def __init__(self):
        # super(busHouse,self).__init__("sr")   #这种方法只能调用第一个父类的构造方法
        car.__init__(self)          #这种方法真正实现随意调用
        house.__init__(self,"beijing house")

c=carHouse()
print c.engine
print c.height
print c.width
print c.get_volumn()
print c.carry_people_bumber()