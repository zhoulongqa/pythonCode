# encoding=utf-8
import MySQLdb
import random

def getDatabaseConnection():
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123123',
        charset='utf8')
    cur = conn.cursor()
    return conn, cur


def closeDatabase(conn, cur):
    cur.close()
    conn.close()


def createDatabase(data_base_name):
    conn,cur = getDatabaseConnection()
    result = cur.execute(
        'create database if not exists %s default charset utf8 collate utf8_general_ci;' % data_base_name)
    print result
    closeDatabase(conn, cur)


def create_table(database_name, table_sql):
    conn,cur = getDatabaseConnection()
    conn.select_db(database_name)
    result = cur.execute(table_sql)
    return result
    closeDatabase(conn, cur)


def insert_data(database_name, data_sql):
    conn,cur = getDatabaseConnection()
    conn.select_db(database_name)
    result = cur.execute(data_sql)
    print result
    closeDatabase(conn, cur)


#createDatabase('wangzeliangDB')
table_sql='''CREATE TABLE user( 'id' int(11) default null,'name' VARCHAR(255) DEFAULT NULL,'passwd' VARCHAR(255) DEFAULT NULL,'birthday' DATA DEFAULT NULL)ENGINE=Innodb DEFAULT  CHARSET=utf8;'''
data_sql = "insert into user values(1,'Tom','123','1990-01-01')"
create_table('wangzeliangDB',table_sql)
insert_data("wangzeliangDB", data_sql)