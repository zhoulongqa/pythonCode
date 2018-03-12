#coding=utf-8
def add(x,y):
    return x+y

print add(1,2)
print add("hello","world")
#print add(1,'abc')
#python的加法运算符是“多态”的，理论上，我们实现的add方法支持任意支持加法的对象，
#但是我们不用关心两个参数x和y具体是什么类型

