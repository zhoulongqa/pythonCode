#encoding=utf-8
import multiprocessing
def do(n):
    #获取当前进程的名字
    name=multiprocessing.current_process().name
    print name,"starting"
    print "worker",n
    return

if __name__=="__main__":
    numlist=[]
    for i in xrange(5):
        p=multiprocessing.Process(target=do,args=(i,))
        numlist.append(p)
        p.start()
        p.join()
        print "Process end."
    print numlist
'''
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，并用其
start()方法启动，这样创建进程比fork()还要简单
join()方法表示等待子进程结束以后再继续往下运行，通常用于进程间的同步
注意：
在Windows上要想使用进程模块，就必须把有关进程的代码写在当前.py文件的if __name__=="__main__":
语句的下面，才能正常使用Windows下的进程模块，Unix/Linux下则不需要
'''
