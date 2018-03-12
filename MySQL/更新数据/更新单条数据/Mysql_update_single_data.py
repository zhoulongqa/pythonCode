#encoding=utf-8
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

#查询一条数据
query=cursor.execute("select * from user")
print u"表中所有数据："
for i in cursor.fetchall():
    print i
#更新一条数据
update=cursor.execute("update user set password='Tom_test' where name = 'Tom'")
print u"修改语句受影响的行数：",update

#查询一条数据
cursor.execute("select * from user where name = 'Tom'")

print cursor.fetchone()


#关闭游标
cursor.close()
#提交事务
conn.commit()
#关闭数据库连接
conn.close()
