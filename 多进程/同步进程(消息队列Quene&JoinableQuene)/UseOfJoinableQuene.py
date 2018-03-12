#encoding=utf-8
from multiprocessing import Process,Queue
def offer(queue):
    #入队列
    queue.put("Hello World")
    queue.put("this is a test program")
    queue.put([1,2,3])
if __name__=="__main__":
    #创建一个队列实例
    q=Queue()
    p=Process(target=offer,args=(q,))
    p.start()
    print q.get()   #出队列
    print q.get()
    print q.get()
    try:
        print q.get(block=True,timeout=2)   #出队列
    except Exception,e:
        print u"超时了"
    p.join()
'''
multiprocessing.Queue类似于queue.Queue,一般用来多个进程间的交互信息。Queue是进程和线程安全的，
它实现了queue.Queue的大部分方法，但task.done()和join()方法没有实现
multiprocessing.joinableQueue是multiprocessing.Queue的子类，增加了task_done()方法和join()方法
task_done():用来告诉queue一个task完成，一般在调用get()时获得一个task，在task结束后调用task_done()
来通知Queue当前task完成
join()：阻塞直到queue中的所有的task都被处理(即task_done方法被调用)
'''

