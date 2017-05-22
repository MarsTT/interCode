#coding=utf-8
from bs4 import BeautifulSoup
import urllib
import re
import pymysql


conn = pymysql.connect(host="127.0.0.1",user='root',passwd='lovol12345',charset='utf8')

cur = conn.cursor()
cur.execute('USE wikipedia')


def insert_page(url):
	#先查询url存在，如果不存在，将其插入表pages中
	#否则直接返回
	cur.execute("select * from pages where url=%s",(url))
	if cur.rowcount == 0:
		cur.execute("insert into pages (url) values (%s)",(url))
		conn.commit()
		#返回当前的游标指向的ID号
		return cur.lastrowid
	else:
		#返回游标查找到的一行数据的第一列(即ID)
		return cur.fetchone()[0]


def insert_link(fromPageId,toPageId):
	# 先查询是否存在fromPageId 和 toPageId
	# 如果不存在，就将其插入表links中
	cur.execute("select * from links where fromPageId=%s and toPageId=%s",(int(fromPageId),int(toPageId)))
	if cur.rowcount == 0:
		cur.execute("insert into links (fromPageId,toPageId) values (%s,%s)",(int(fromPageId),int(toPageId)))
		conn.commit()

pages = set()

def get_links(pageUrl,recursionLevel):
	global pages
	if recursionLevel > 4:
		return 

	pageId = insert_page(pageUrl)
	html = urllib.urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj = BeautifulSoup(html,"html.parser")
	pattern = re.compile('^(/wiki/)((?!:).)*$')
	for link in bsObj.findAll("a",href=pattern):
		insert_link(pageId,insert_page(link.attrs['href']))
		if link.attrs['href'] not in pages:
			newPage = link.attrs['href']
			pages.add(newPage)
			get_links(newPage,recursionLevel+1)


get_links("/wiki/Kevin_Bacon",0)
cur.close()
conn.close()
