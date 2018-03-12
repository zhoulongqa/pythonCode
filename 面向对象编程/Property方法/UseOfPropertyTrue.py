#encoding=utf-8
from datetime import datetime
class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth=datetime.strptime(value,"%Y-%m-%d")
        print self._birth

    @property
    def age(self):
        currentTime=datetime.now()
        currentDate=currentTime.strftime("%Y-%m-%d")
        timedelta=datetime.strptime(currentDate,"%Y-%m-%d")-self._birth
        return timedelta.days/365

if __name__=="__main__":
    s=Student()
    s.birth="1990-08-24"
    print u"现在年龄：",s.age

#上面的birth是可读可写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来



