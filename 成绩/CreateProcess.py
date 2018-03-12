#encoding=utf-8
import multiprocessing
def func1():
    print "func1 is invoked"
def func2():
    print "func2 is invoked"

if __name__=="__main__":
    p1=multiprocessing.Process(target=func1)
    p2=multiprocessing.Process(target=func2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print "Done process"
