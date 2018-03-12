#encoding=utf-8
'''
MySQLdb模块执行sql语句的重要方法由execute和executemany

execute(query,args=None)
execute执行单条sql语句，成功后返回受影响的行数，长整型；
参数说明：
query：要执行的sql语句，字符串类型
args：可选的序列或映射，用于query的参数值，如果args为序列，query中必须使用%s做占位符；如果args为映射，
query中必须使用%(key)s做占位符

executemany(query,args)
该方法用于批量执行sql语句，比如批量插入数据，返回受影响的行数，长整型
参数说明：
query：要执行的sql语句，字符串类型
args：嵌套的序列或映射，用于query的参数值
数据库性能瓶颈很大一部分就在于网络IO和磁盘IO，将多个sql语句放在一起，只执行一次IO，
可以有效的提升数据库性能，推荐此方法

注意：
用executemany()方法一次性批量执行sql语句，固然很好，但是当数据一次传入过多到server端，
可能造成server端的buffer溢出，也可能产生一些意向不到的麻烦，所以，合理、分批次使用executemany是个
合理的方法
'''

