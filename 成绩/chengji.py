#encoding=utf-8
def chengji():
    Exelence_score=0
    Good_score=0
    Pass_score=0
    NotPass_score=0
    for i in range(10):
        score = int(raw_input("please input the score:"))
        if score>100 or score<0:
            print "It is a invalid input"
        elif score>80 and score<=100:
            print "Exelence"
            Exelence_score+=1
        elif score>70 and score<=80:
            print "good"
            Good_score+=1
        elif score>=60 and score<=70:
            print "Pass"
            Pass_score+=1
        elif score<60:
            print "NotPass the test"
            NotPass_score+=1
    print u"优秀的人数是：",Exelence_score
    print u"良好的人数是：",Good_score
    print u"及格的人数是：",Pass_score
    print u"不及格的人数是：",NotPass_score
chengji()




