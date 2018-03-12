#encoding=utf-8
import MySQLdb
try:
    conn=MySQLdb.connect(
        host='127.0.0.1',
        user='root',
        passwd='123123',
        port=3306)
    conn.select_db('testcreatedatabase')  #选择pythonDB数据库
    cur=conn.cursor()   #获取游标
    #如果所建表已经存在，删除重建
    cur.execute("drop table if exists User;")
    #执行建表语句
    cur.execute("create table User(id int(11) default null,name varchar(255) default null,password varchar(255) default null,birthday date default null)engine=innodb default charset=utf8;")
    cur.close()
    conn.close()
    print u"创建数据表成功"
except MySQLdb.Error,e:
    print "MySQL Error %d:%s" % (e.args[0],e.args[1])