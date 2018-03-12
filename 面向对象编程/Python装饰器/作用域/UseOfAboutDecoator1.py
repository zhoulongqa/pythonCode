#encoding=utf-8
'''
python中，函数会创建一个自己的作用域，有的人会叫之为命名空间，这意味着在函数
内部访问某个变量时，函数会优先在自己的命名空间中寻找
'''
outerVar="this is a global variable"
def test():
    innerVar="this is a local variable"
    print "local variables:"
    print locals()
test()
print "global variables"
print globals()
'''
内置函数globals返回的是python解释器能知道的变量名称的字典(变量名：值)
而locals函数返回的是函数test内部本地作用域中的变量名称字典，由此可以看出
函数都是有自己独立的命名空间的
'''