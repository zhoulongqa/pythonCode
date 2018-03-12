#encoding=utf-8
import MySQLdb
conn=MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123123',
    db="gloryroad",
    charset="gbk")
#使用cursor()方法获取数据库操作游标
cursor=conn.cursor()
print conn
print type(conn)
'''
执行如果没报任何错误，说明数据库已经连接成功
从执行结果来看，connect函数返回的一个连接mysql成功后的实例，用这个实例可以进行
后续操作，比如查询数据，插入数据等
注意：
这里只是连接了数据库，要向操作数据库，还必须创建游标

通过获取到的数据库连接实例conn下的cursor()方法来创建游标，游标用来接收返回结果

Mysql本身不支持游标，但是mysqldb对游标进行了仿真。cursor()函数也是返回一个游标的实例对象，
在这个实例对象中，内建了很多操作数据的方法，比如执行sql语句

'''