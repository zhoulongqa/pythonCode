#encoding=utf-8
def divide_by_include_9():
    '''打印出数字能否被包含9的数整除'''
    a=int(raw_input("please input a num:"))
    for i in xrange(1,a):
        if "9" in str(i) and a%i==0:
            print i
divide_by_include_9()