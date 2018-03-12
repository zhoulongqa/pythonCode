#encoding=utf-8
'''
将json格式字符串解码成Python对象，我们使用的是json.loads()函数，可以将简单数据类型编码成python对象
编码过程中，python中的list和tuple都被转化成json的数组，而解码后，json数组最终转化成python的list的，
无论原来是list还是tuple
'''
import json
data=[{'a':'Aasdf','b':(2,4),'c':3.0}]
data_json=json.dumps(data)
print "encoding:",data_json
print "decoding:",json.loads(data_json)


'''
从json到python的类型转换
JSON字符串类型           Python类型
object                  dict
array                   list
String                  unicode
number(int)             int,long
number(real)            float
true                    True
false                   False
null                    None
'''
a=[{1:12,'a':12.3},[1,2,3],(1,2),'asd',u'ad',12,13L,3.3,True,False,None]
print u"编码后：\n",json.dumps(a)
print u"解码后：\n",json.loads(json.dumps(a))



