#encoding=utf-8
'''
apply函数准备接收一个函数的变量，它也只是一个普通的变量，和其他变量一样。然后我们
调用传进来的函数："()代表着调用的操作并且调用变量包含的值"。在函数外，我们也能看到
传递函数并没有什么特殊的语法，函数的名称只是和其他变量一样的标识符而已
'''
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def apply(func,x,y):
    return func(x,y)
print apply(add,2,1)
print apply(sub,2,1)