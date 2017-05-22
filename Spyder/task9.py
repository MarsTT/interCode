#coding=utf-8

import urllib
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

#创建连接属性，连接数据库
conn = pymysql.connect(host='127.0.0.1',user='root',passwd='lovol12345',db='mysql',charset='utf8')

#创建游标
cur = conn.cursor()
#执行数据库
cur.execute("USE scraping")

random.seed(datetime.datetime.now())

#定义存储标题和内容的方法
def store(title,content):

	'''
		光标操作和连接操作分离，当光标里存储了与数据上下文的信息时
		需要通过连接确认操作先将信息传进数据库，再将信息插入数据库
	'''

	#利用游标向数据库中插入影响的title以及内容
	cur.execute("insert into pages(title,content) values (\"%s\",\"%s\")",(title,content))
	#然后利用游标将数据提交给数据库（连接确认）
	cur.connection.commit()

def get_links(article_url):
	#打开网站连接
	html = urllib.urlopen("http://en.wikipedia.org"+article_url)
	#将内容格式化
	bsOjb = BeautifulSoup(html,"html.parser")
	#找到h1标签，输出文本
	title = bsOjb.find("h1").get_text()
	content = bsOjb.find("div",id="mw-content-text").find("p").get_text()
	store(title,content)
	# 正则表达式，找到所有以/wiki/开头的网页
	pattern = re.compile(r'^(/wiki/)((?!:).)*$')
	return bsOjb.find("div",id="bodyContent").findAll("a",href=pattern)


links = get_links("/wiki/Kevin_Bacon")

try:
	#在所有内连接网站随机选择一个继续往下爬去
	while len(links) > 0:
		newArticle = links[random.randint(0,len(links)-1)].attrs['href']
		print newArticle
		link = get_links(newArticle)
finally:
	#一定要记得关闭cur和conn
	cur.close()
	conn.close()
