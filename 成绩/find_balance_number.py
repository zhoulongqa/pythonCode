#encoding=utf-8
def add(a,b):
    return a+b
def find_balance_number(listNumber):
    if isinstance(listNumber,(list,tuple)):
        for i in range(len(listNumber)):
            if reduce(add,listNumber[0:i],0)==reduce(add,listNumber[i+1:],0):
                print reduce(add,listNumber[0:i],0)
                print "position:",i
                print "value:",listNumber[i]
                break
    else:
        print "need a list or tuple containing numbers"
        return None

list1=[1,2,3,5,2,3,1]
find_balance_number(list1)