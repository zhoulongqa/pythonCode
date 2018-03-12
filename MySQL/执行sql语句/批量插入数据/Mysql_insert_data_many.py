#encoding=utf-8
'''
批量执行sql语句使用的是executemany(sql,args)函数，返回受影响的行数，args参数是一个包含多个元素的列表，
每个元素对应mysql中的一条数据，注意：这里的%s不需要加引号，否则插入数据的数据会类型错误
'''
import MySQLdb
conn=MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123123',
    db='testcreatedatabase',
    charset='utf8')
#使用curson()方法获取数据库的操作游标
cursor=conn.cursor()
#批量插入数据
sql="insert into user values(%s,%s,%s,%s)"
insert=cursor.executemany(sql,[(4,'cat','cat','1989-02-12'),
                               (5,'lily','linux','1993-03-14'),
                               (6,'Lucy','python','1998-03-28')])
print u"批量插入返回受影响的行数：",insert
#关闭游标
cursor.close()
#提交事务
conn.commit()
#关闭数据库连接
conn.close()
print u"sql语句执行成功"