#encoding=utf-8
import time
fp=open("d:\\xx.py",'w+')
for i in range(30):
    fp.write("glory test"+str(i)+'\n')
fp.close()

fp=open("d:\\xx.py",'r')
i=1
for line in fp:
    if i%5==0:
        print "*"*20
        time.sleep(1)
        raw_input("press enter to continue")
    print line
    i+=1
fp.close()