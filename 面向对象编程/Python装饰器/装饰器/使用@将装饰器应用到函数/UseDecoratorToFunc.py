#encoding=utf-8
'''
Python 2.4以后，支持使用标识符@将装饰器应用到函数上，只需要在函数的定义前加上@装饰器的名称即可
'''
import time
def log(func):
    def wrapper(*arg,**kw):
        print "call func is %s" % func.__name__
        return func(*arg,**kw)
    return wrapper

@log
def now():
    now=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    print "current time is %s" % now
now()
'''
观察log函数，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数，
调用now()函数时，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志

把@log放到now()函数的定义处，就相当于执行了如下语句：
now=log(now)

由于log()是一个decorator，返回一个函数，所以，原本的now()函数仍然存在，只是
现在同名的now()变量指向了新的函数，于是调用now()将执行新函数，即在log()函数
中返回的wrapper()函数

wrapper()函数的参数定义是(*args,**kw)，因此，wrapper()函数可以接受任意参数的
调用，在wrapper()函数内，首先打印日志，再紧接着调用原始函数

正因为有了(*args,**kw)这样的参数形式，意味着装饰器能够接受拥有任何签名的函数作为
自己的被装饰方法，同时能够用传递给它的参数对被装饰的方法进行调用，这样就能处理
参数个数不同的函数了

'''