#coding=utf-8
import pymysql

'''
	连接/光标模式 是数据库中常用的两种模式：
	连接模式，除了要连接数据库之外，还要发送数据库信息，处理回滚操作，创建新的光标对象
	回滚：当一个查询或一组查询被中断的时候，数据库回到初始状态，一般用事务控制手段实现回滚


	光标模式：一个光标跟踪一种状态信息，比如跟踪数据库的使用状态
	包含最后一次查询执行的结果。
	通过调用光标函数，可以获取查询结果
'''




# 连接对象
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='lovol12345',db='mysql')

# 光标对象
cur = conn.cursor()

cur.execute("USE scraping")

cur.execute("select * from pages where id='1'")

print cur.fetchone()

cur.close()
conn.close()