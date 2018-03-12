#encoding=utf-8
def outer():
    name="python"
    def inner():
        print name
    return inner
res=outer()
res()
print res.func_closure
'''
inner作为一个函数被outer返回，保存在变量res中，并且还能够调用res()
通过上面对遍历的作用域和生存周期我们不难明白，name是函数outer里的一个
局部变量，也就是说只有当outer正在运行时，该变量才会存在，根据python的
运行模式，我们是没法在函数outer执行退出之后还能继续调用inner函数的，并
且在inner函数被调用时，变量name早已不存在了，但为什么调用成功了？
这就回到了我们的闭包这个问题上了，python支持一个叫函数闭包的特性

如果一个函数定义在另一个函数的作用域内，并且引用了外层函数的变量，则该函数
称为闭包
闭包是python所支持的一种特性，它让在非global scope定义的函数可以引用其外围
空间中的变量，这些外围空间中被引用的变量叫做这个函数的环境变量。环境变量和这个
非全局函数一起构成了闭包

上例中的inner()函数就是一个闭包，它本身也是一个函数，而且还可以访问本身之外的变量

这能够通过查看函数的func_clousure属性得出结论，这个属性里面包含封闭作用域里面的值
(只会包含被捕捉到的值，比如name，如果在outer里还定义了其他的值，封闭作用域里面是不会有的)

每次函数outer被调用时，inner函数都会被重新定义，上面每次返回的函数inner结果都一样，因为name
没变
'''