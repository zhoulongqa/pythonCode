#encoding=utf-8
def array_add():
    n=int(raw_input("please input array dimension number:"))
    sum=0
    for i in xrange(1,n+1):
        for j in xrange(1,n+1):
            if j==n:
                print j
            else:
                print j,
            if i==j:
                sum=sum+j
    print u"n*n的对角线之和为：",sum

def array_adds():
    n=int(raw_input("please input array dimensionnumber:"))
    sum=0
    x=0
    for i in xrange(1,n+1):         #控制行号
        for j in xrange(1,n+1):     #控制列号
            x+=1
            if x<=9:
                print '',   #打印一个空格，不要在''中加空格
            if j==n:
                print x
            else:
                print x,
            if i==j:        #对于行号与列号相等的时候
                sum=sum+x
    print u"n*n的对角线之和为：",sum

#array_add()
array_adds()