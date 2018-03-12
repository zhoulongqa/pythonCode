#encoding=utf-8
'''
使用json.dumps()方法来将一个python数据类型列表编码成json格式的字符串
'''
import json
data=[{'a':'A','b':(2,4),'c':3.0}]
res=repr(data)
print "data:",res
data_json=json.dumps(data)
print data_json
print type(data_json)
'''
观察两次打印的结果，会发现python对象转成JSON字符串以后，跟原始的repr()
输出的结果会有些特殊的编号，原字典中元组被改成了json类型的数组
在json的编码过程中，会存在从Python原始类型转换为json类型的过程，但这两种
语言的类型存在一些差异，如下表


python类型            JSON字符串类型
dict                object
list,tuple          array
int,long,float      number
str,unicode         string
True                true
False               false
None                null
'''

#Python类型与json类型示例比对
a=[{1:12,'a':12.3},[1,2,3],(1,2),'asd',u'ad',12,13L,3.3,True,False,None]
print u"Python类型：\n",a
print u"编码后的json串：\n",json.dumps(a)

'''
json.dumps()
函数原型：
dumps(obj,skipkeys=False,ensure_ascii=True,check_circular=True,allownan=True,
cls=None,indent=None,separators=None,encoding="utf-8",default=None,sort_keys=False,
**kw)
该方法返回编码后的一个json字符串，是一个str对象encodedjson
dumps函数的参数很多，但是不是所有的都必须弄清楚
1.sort_keys：是否按字典顺序(a-z)输出，因为默认编码成json格式字符串后，是紧凑输出，
并且也没有顺序的，不利于可读
'''
data=[{'a':'A','b':(2,4),'c':3.0}]
print json.dumps(data)
print json.dumps(data,sort_keys=True)
print "--------------------indent-------------------------------"
#2.indent:设置参数缩进显示的空格数，缩进显示使读起来更加清晰
print json.dumps(data,sort_keys=True,indent=3)
print "--------------------separators---------------------------"
'''
sepatators:参数的作用是去掉逗号和分号后面的空格，从上面的输出结果都能看到，
","与";"后面都有个空格，这都是为了美化输出结果的作用，但是在我们传输数据的过程中，
越精简约好，冗余的东西全部去掉，因此就可以加上separators参数对传输的json串进行压缩。
该参数是元组格式的
'''
print len(json.dumps(data))
#去掉编码后的json串中，和:后面的空格
print len(json.dumps(data,separators=(',',';')))

print "=========================skipkeys========================"
'''
skipkeys:在encoding过程中，dict对象的key只可以是基本数据类型
(str,unicode,int,long,float,bool,None),如果是其他类型，那么在编码过程中就会抛出
TypeError的异常，skipkeys可以跳过那些非string对象的key的处理，就是不处理
'''
data=[{'a':'A','b':(2,4),'c':3.0,(1,2):'D tuple'}]
print u"不设置skipkeys参数"
try:
    res1=json.dumps(data)       #skipkeys参数默认为False时
except Exception,e:
    print e
print u"设置skipkeys参数"
print json.dumps(data,skipkeys=True)    #skipkeys=True时

'''
ensure_ascii:表示编码使用的字符集，默认是True，表示使用ascii码进行编码。
如果设置为False，就会以Unicode进行编码。由于解码json字符串时返回的就是Unicode
字符串，所以可以直接操作Unicode字符，然后直接编码Unicode字符串，这样会简单些
'''
