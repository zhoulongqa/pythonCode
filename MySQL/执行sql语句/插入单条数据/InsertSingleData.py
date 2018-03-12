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
#插入一条数据
insert=cursor.execute("insert into User values(1,'Tom','123','1990-08-24')")
print u"添加语句受影响的行数：",insert

#另一种插入数据方法，通过格式字符串传入值
sql="insert into User values(%s,%s,%s,%s)"
cursor.execute(sql,(3,'Lucy','efg','1992-05-17'))
#关闭游标
cursor.close()
#提交事务
conn.commit()
#关闭数据库连接
conn.close()
print u"sql语句执行成功"