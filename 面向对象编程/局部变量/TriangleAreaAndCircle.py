#encoding=utf-8
class Triangle(object):
    def __init__(self,bottom,height):
        self.bottom=bottom
        self.height=height
    def getAreaOfTriangle(self):
        area=0.5*self.bottom*self.height
        return area
    def getCircleTriangle(self):
        circle=2*(self.bottom+self.height)
        return circle
a=Triangle(100,200)
print a.getAreaOfTriangle()
print a.getCircleTriangle()