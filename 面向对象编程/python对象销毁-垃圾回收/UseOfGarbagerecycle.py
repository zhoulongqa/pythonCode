#encoding=utf-8
import sys
print sys.getrefcount(500111)
a=500111    #创建对象
print sys.getrefcount(a)
b=a         #增加引用，<500111>的计数
print sys.getrefcount(500111)
c=[b]       #增加引用,<500111>的计数
print sys.getrefcount(500111)
del a       #减少引用，<500111>的计数
print sys.getrefcount(500111)
b=100       #减少引用，<500111>的计数
print sys.getrefcount(500111)
c[0]=-1     #减少引用，<500111>的计数
print sys.getrefcount(500111)