#encoding=utf-8
def outer(name):
    def inner():
        print name
    return inner
res1=outer("python")
res2=outer("java")
res1()
res2()