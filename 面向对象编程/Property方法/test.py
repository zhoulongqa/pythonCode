#coding:utf-8


# class Parent(object):	#define parent class
#     parentAttr=100	#类变量
#     def __init__(self):
#         self.name="zhangsan"
#     print "Calling parent construct"



# P = Parent()
# print P
# print P.parentAttr
# print P.name
# print Parent().parentAttr

# getattr(P,'parentAttr')
# getattr(P,'name')

# hasattr(P,'parentAttr')
# setattr(P,'parentAttr',10)
# print P.parentAttr



# #局部变量
# class Person(object):
#     id=12
#     def __init__(self,name):
#         self.name=name	#类的实例变量
#  		# self.inName='ads'	#类的实例变量
#     def getName(self):
#  		name='Lucy'	#局部变量
#  		return self.name,name
# p=Person("linda")
# print p.name	#访问对象的实例变量
# #通过函数访问实例变量和局部变量
# res=p.getName()
# print res


# #类方法
# class Person(object):
#     id=12	#类静态成员在这定义，注意缩进
#     def __init__(self,name):
#         self.name=name
#         self.__inName='ads'
#     @classmethod 	#类方法定义，用注解方式说明
#     def up(cls,a):	#这是cls，而不是self
#  		print cls#,cls__name__
# 		return a+1
# #创建类的实例
# p=Person("aplha")
# #调用类方法
# print Person.up(20)	#类名直接调用
# print p.up(12)	#通过实例对象调用




'''修改类属性的值，有三种方法，分别是：
1、通过类方法修改
2、通过实例方法修改
3、直接通过类对象修改
'''
# class employee(object):
#     city='Bj'   #类属性
#     def __init__(self,name):
#         self.name=name  #实例变量

#     #定义类方法
#     @classmethod
#     def getCity(cls):
#         return cls.city

#     #定义类方法
#     @classmethod
#     def setCity(cls,city):
#         cls.city=city
#     #实例方法
#     def set_City(self,city):
#         employee.city=city

# emp=employee('joy') #创建类的实例
# print emp.getCity() #通过对象实例引用类方法，'bj'
# print employee.getCity()    #通过类对象引用类方法  'bj'

# emp.setCity('T')#实例对象调用类方法改变类属性的值
# print emp.getCity()
# print employee.getCity()

# employee.setCity('CD')  #类对象调用类方法改变类属性的值
# print emp.getCity()
# print employee.getCity()

# employee.city=20 #直接修改类属性的值
# print emp.getCity()
# print employee.getCity()


'''
静态方法：
静态方法是在类内部使用关键字def定义的方法，但与其他方法不同的是，需要用修饰器"@staticmethod"来标识其为静态方法，并且在定义静态方法时不需要传入任何隐式参数
静态方法既可以直接使用类名去调用，还可以使用类的实例去调
'''

# #coding=utf-8
# class Person(object):
#     id=12	#类静态成员在这定义，注意缩进
#     def __init__(self,name):
#         self.name=name
#  		# self.__inName='ads'

# 	@staticmethod	 	#类静态方法定义，用注解方式说明
# 	def down(b):		#  静态方法不需要self，cls变量
# 		id=13
#     	print u"类变量id=",id
#     	return b-1
# #创建类的实例
# p=Person("alpha")
# #调用静态方法
# print Person.down(15)	#类名直接调用
# print p.down(19)		#通过实例对象调用