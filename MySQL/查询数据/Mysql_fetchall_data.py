#encoding=utf-8
'''
获取游标所在处开始及以下所有的数据，并以元组的形式返回，元组的每一个元素也是由
一行数据组成的元组，如果游标所在处没有数据，将返回空元组，执行完这个方法后，游标
将移动到数据库表的最后
'''
import MySQLdb
#打开数据库连接
conn=MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123123',
    db='testcreatedatabase',
    charset='utf8')
#使用cursor()方法获取数据库的操作游标
cursor=conn.cursor()
cursor.execute("select * from user")

resSet=cursor.fetchall()
print u"共%s条数据"% len(resSet)
print resSet

#关闭游标
cursor.close()
#提交事务
conn.commit()
#关闭数据库连接
conn.close()
print u"sql语句执行成功"