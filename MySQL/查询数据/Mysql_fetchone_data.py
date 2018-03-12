#encoding=utf-8
'''
从execute()函数的查询结果中取数据，以元组的形式返回游标所在处的一条数据，如果游标
所在处没有数据，将返回空元组，该数据执行一次，有效向下移动一个位置。fetchone()函数必须
跟execute()函数结合使用，并且在execute()函数之后使用
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
while 1:
    res=cursor.fetchone()
    if res is None:
        #表示已经取完结果集
       break
    print res
cursor.close()
#提交事务
conn.commit()
#关闭数据库连接
conn.close()
print u"sql语句执行成功"