#encoding=utf-8
class f(object):
    count=12    #类变量
t=f()
print u"t.count内存地址=",id(t.count),"t.count=",t.count   #实例变量
print u"f.count内存地址=",id(f.count),"f.count=",f.count   #类变量
t.count=10
print u"通过实例对象修改count的值后"
print u"t.count内存地址=",id(t.count),"t.count=",t.count   #10
print u"f.count内存地址=",id(f.count),"f.count=",f.count   #12
'''
从上例两句类变量访问来看，类变量既可以通过类变量名直接调用，也可以通过实例对象名调用
但是当执行t.count=10
再次打印t.count的值会变成10，而f.count的值仍然是12，并且内存地址也不一样了。

类名.属性名=value这种方式添加的，那这个属性就是类的类属性，其所有的实例对象都可以访问，但是
如果是通过类的某个实例对象去添加的，像实例名.属性名=value，这种添加方式，那这个属性只属于这
个实例对象所有，并且如果添加的属性名与类中类属性名相同的时候，类属性在这个实例对象中就会被屏
蔽掉，也就是说实例引用时，同名的实例属性会屏蔽同名的类属性，就类似于全局变量与局部变量的关系
所以当执行t.coutn=10语句后，就等于给实例对象添加了一个同名的类属性count，其值等于10，但父类
的该类属性的值并未被改变，所有此时打印t.count，就是引用的是t实例中的count属性
'''
