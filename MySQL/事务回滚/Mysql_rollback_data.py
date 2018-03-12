#encoding=utf-8
'''
事务：就是一系列SQL语句的集合
在操作数据时，当一个事务执行出错了，就需要将数据库回滚到所有事务执行前正确的状态，
以保持数据的完整性
数据回滚需要在游标关闭之前
'''
import MySQLdb
conn=MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123123',
    db='pythondb',
    charset='utf8')

#使用cursor方法获取数据库的操作游标
cursor=conn.cursor()
cursor.execute("insert into User values(1,'Tom','123','1990-08-24')")
cursor.execute("select * from user")
cursor.execute("select * from user")
datas=cursor.fetchall()
print u"修改前的数据：\n",datas[0]

#更新表中一条数据
cursor.execute("update user set birthday='2100-08-21' where name = 'Tom'")
cursor.execute("select * from user")
datas=cursor.fetchall()
print u"修改后的数据：\n",datas[0]

#回滚事务
conn.rollback()
cursor.execute("select * from user")
datas=cursor.fetchall()
#print u"事务回滚后的数据：\n",datas[0]


cursor.close()
conn.commit()
conn.close()
