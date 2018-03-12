#encoding=utf-8
from multiprocessing import Process,Queue
import os,time,random

#写数据进程执行的代码
def write(q):
    for value in ['A','B','C']:
        print 'Put %s to queue..'% value
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    while not q.empty():
        print "Get %s from queue" % q.get(True)
        time.sleep(1)   #目的是等待写队列完成

if __name__=="__main__":
    #父进程创建Queue，并传给各个子进程
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    #启动子进程pw，写入
    pw.start()
    #启动子进程pr，读取
    pr.start()
    #等待pw结束
    pw.join()
    pr.join()
'''
由于操作系统对进程的调度时间不一样，所以该程序每次执行的结果均不一样。程序读队列函数中为什么
要加一句time.sleep(1)，目的是等待写程序将数据写到队列中，防止有时写进程还没有将数据写进队列，
读进程就开始读了，导致读不到数据。但是这种并不能有效的预防此种情况的出现。
'''