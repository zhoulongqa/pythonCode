#encoding=utf-8
import MySQLdb
try:
    conn=MySQLdb.connect(
        host='127.0.0.1',
	user='root',
	passwd='123123',
	port=3306)
    cur=conn.cursor()
    cur.execute("create database if not exists TestCreateDatabase default character set utf8")
    cur.close()
    conn.close()
    print u"创建数据库TestCreateDatabase成功!"
except MySQLdb.Error,e:
    print "Mysql error %d:%s" % (e.args[0],e.args[1])
