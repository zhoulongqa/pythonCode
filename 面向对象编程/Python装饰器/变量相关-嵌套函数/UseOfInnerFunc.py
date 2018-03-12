#encoding=utf-8
'''
python允许创建嵌套函数，也就是我们可以在函数里面定义函数，而且现有的作用域和变量生存周期依旧不变

在inner函数中，python解析器需要找一个叫name的本地变量，查找失败后会继续在上层的作用域里面寻找，
这个上层作用域定义在outer函数里，python函数可以访问封闭作用域。
对于outer函数中最后一句，在调用inner函数，需要知道非常重要的一点就是，inner也仅仅是一个遵循python变量
解析规则的变量名，python解释器会优先在outer的作用域里面对变量名inner查找匹配的变量。

把恰好是函数标识符的变量inner作为返回值返回回来，每次函数outer被调用的时候，函数inner都会
被重新定义，如果它不被当做变量返回的话，每次执行过后它将不复存在

在python里，函数就是对象，它也只是普通的值而已，也就是说你可以把函数像参数一样传递给
其他的函数或者说函数里面返回函数
'''
def outer():
    name="python"
    def inner():
        print name
    return inner()
outer()
