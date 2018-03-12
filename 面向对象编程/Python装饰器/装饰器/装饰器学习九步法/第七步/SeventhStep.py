#encoding=utf-8
'''
在第四步的基础上，让装饰器带参数
和上一实例比起来在外层多了一层包装，装饰函数名实际上应更有意义些
'''
def deco(arg):
    def _deco(func):
        def __deco():
            print "before %s called [%s]" % (func.__name__,arg)
            func()
            print "after %s called [%s]" % (func.__name__,arg)
        return __deco
    return _deco

@deco("mymodule")
def myfunc():
    print "myfunc() called"

@deco("module2")
def myfunc2():
    print "myfunc2() called"
myfunc()
myfunc2()