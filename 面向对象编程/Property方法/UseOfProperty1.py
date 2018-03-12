#encoding=utf-8
class Student():
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.__score=score
    def set_score(self,score):
        if isinstance(score,int):
            raise ValueError("score must be an interger")
        if score<0 or score >100:
            raise ValueError("score must be between 0-100")
        self.__score=score

    def get_score(self):
        return self.__score
s=Student('tom',19,90)
print "score is:",s.get_score()
try:
    s.set_score(999)
except Exception,e:
    print "score error!"
