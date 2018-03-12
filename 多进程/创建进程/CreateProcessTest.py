#encoding=utf-8
import multiprocessing
def func1(n):
    print n
    return n
def func2(a,b):
    print a+b

if __name__=="__main__":
    p1=multiprocessing.Process(target=func1,args=(10,))
    p2=multiprocessing.Process(target=func2,args=(1,2))

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    print "done"
