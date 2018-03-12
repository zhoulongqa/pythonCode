#encoding=utf-8
'''
在python的作用域规则里面，创建变量时一定会在当前作用域里创建同样的变量，但访问
或修改变量时，会在当前作用域中查找该变量，如果没找到匹配的变量，就会依次向上在
闭合作用域中进行查找，所以在函数中直接访问全局变量也是可以的
'''
outerVar="this is a global variable"
n=10
def test():
    innerVar="this is a local variable"
    print outerVar
    print n

test()