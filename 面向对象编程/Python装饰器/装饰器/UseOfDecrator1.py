#encoding=utf-8
'''
装饰器就是一个闭包，把一个函数当做参数后返回一个替代版函数
'''
import time
def now():
    print "current time is %s" % time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
res=now()
#res()
'''
现在如果想给now()函数增加一些别的功能，比如在调用该函数前后自动打印一些日志
但又不希望修改原now()的定义，这时我们的装饰器就派上用场了
本质上，decorator就是一个返回函数的高阶函数，所以需要定义一个能打印日志的decorator'''
'''
def log(func):
    def wrapper(*args,**kw):
        print "call %s" % func.__bane__
        return func(*arg,**kw)
    return wrapper
'''