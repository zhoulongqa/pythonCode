#!/user/bin/python
#encoding=utf-8
'''只能在linux下执行
fork()函数，属于一个内建函数，并且只在linux系统下存在。特殊，普通的调用函数，调用一次，返回一次
但是fork()调用一次，返回两次，因为操作系统自动把当进程(称为父进程)复制了一份(称为子进程)，然后分别
在父进程和子进程内返回
子进程永远返回0，而父进程返回子进程的ID，这样做的理由是，一个父进程可以fork()出很多子进程，所以，父
进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID，子进程只需要调用os.getpid()
函数可以获取自己的进程号
'''
import os
print os.getpid()

pid=os.fork()   #创建一个子进程
print pid
if pid==0:
    print "I am child process(%s) and my parent is %s."%(os.getpid,os.getppid())
else:
    print "I (%s) just created a child process (%s)." %  (os.getpid(),pid)
