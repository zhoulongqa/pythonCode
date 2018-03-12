#encoding=utf-8
'''
重置游标位置
通过fetchone()、fetchmany()、fetchall()这些方法提取数据后，游标会向后移动相应个数
的位置，如果我们想回头去查询已经查询过的数据，这个时候就需要重置游标的位置了，正好
MySQLdb提供了一个重置游标的方法：scroll(value,mode='relative')
移动指针到参数value指定的行。如果mode='relative',则表示从当前所在行前移value行，
如果mode='absolute',则表示相对结果集的第一行向前移动value行。游标索引从0开始'''
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
print u"当前游标所在位置：",cursor.rownumber
print u"表中所有数据："
for i in cursor.fetchall():
    print i

print u"当前游标所在位置：",cursor.rownumber
print u"将游标重置到索引号为0的位置"
s=cursor.scroll(0,mode="absolute")
print u"当前游标所在位置:",cursor.rownumber


data=cursor.fetchone()
print u'获取游标所在处的一条数据：\n',data

print u"当前游标的位置:",cursor.rownumber
print u"将游标前移2个位置"
cursor.scroll(2,mode='relative')

print u"当前游标的位置:",cursor.rownumber
datas=cursor.fetchmany(2)
print u"获取游标所在处开始的三行数据："
for i in datas:
    print i
print u"当前游标所在位置：",cursor.rownumber

print u"将游标移回索引号为3的位置："
cursor.scroll(3,mode='absolute')

print u"当前游标的位置",cursor.rownumber
data=cursor.fetchone()
print u"获取游标所在处一行数据:\n",data
#关闭游标
cursor.close()
#提交事务
conn.commit()
#关闭数据库连接
conn.close()
print u"sql语句执行成功"