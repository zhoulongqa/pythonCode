#encoding=utf-8
lines=int(raw_input("please input lines of num:"))
result=range(1,(1+lines)*lines/2+1)
for i in range(1,lines+1):
    temp,result=result[:i],result[i:]
    print '*'.join(map(str,temp))