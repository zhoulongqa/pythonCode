#encoding=utf-8
'''
从execute()函数结果中获取游标所在处的size条数据，并以元组的形式返回，元组
的每一个元素都也是由一行数据组成的元组，如果size大于有效的结果行数，将会
返回cursor.arraysize条数据，但如果游标所在处没有数据，将返回空元组，查询几条
数据，游标将会向下移动几个位置，fetmany()函数必须跟execute()函数结合使用，
并且在execute()函数之后使用
'''
import MySQLdb
#打开数据库连接
conn=MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123123',
    db='pythondb',
    charset='utf8')
#使用cursor()方法获取数据库的操作游标
cursor=conn.cursor()
cursor.execute("select * from user")
#获取游标处两条数据
resTuple=cursor.fetchmany(2)
print u"结果集类型：",type(resTuple)
for i in resTuple:
    print i
#关闭游标
cursor.close()
#提交事务
conn.commit()
#关闭数据库连接
conn.close()
print u"sql语句执行成功"