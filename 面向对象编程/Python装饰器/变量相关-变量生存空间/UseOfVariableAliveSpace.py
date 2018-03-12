#encoding=utf-8
'''
变量不仅仅是存在于一个个的命名空间中，它们还都有自己的生存周期，全局变量的生存
周期是在整个执行期间有效，而局部变量的生存周期只在当前作用域中有效，一旦这个作用
域不存在了，比如函数执行退出了，变量的生存周期就结束了
'''
outerVar="this is a global variable"
def test():
    innerVar="this is a local variable"
test()
print outerVar
#print innerVar
#在上例中，innerVar变量是函数中的局部变量，所以在函数执行结束后，再去访问该变量，就会报NameError错误