#encoding=utf-8
'''
让装饰器类带参数
'''
class locker:
    def __init__(self):
        print "locker.__init__() should be not called"
    @staticmethod
    def acquire():
        print u"locker.acquire() called(这是静态方法)"

    @staticmethod
    def release():
        print u"locker.release() called.(不需要对象实例)"

def deco(cls):
    "cls必须实现acquire和release静态方法"
    def _deco(func):
        def __deco():
            print "before %s called [%s]" % (func.__name__,cls)
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return __deco
    return _deco

@deco(locker)
def myfunc():
    print "myfunc() called"

myfunc()
myfunc()