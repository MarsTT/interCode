#coding=utf-8

'''
url :"http://money.163.com/special/pinglun/"
抓取第一页的新闻信息，并按照以下规格输出。

[
  {'title':'生鲜电商为何难盈利？',
  'created_at':'2013-05-03 08:43',
  'url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}

  {'title':'生鲜电商为何难盈利？',
  'created_at':'2013-05-03 08:43',
  'url':'http://money.163.com/13/0503/08/8TUHSEEI00254ITK.html'}

]
'''
import pymysql
import urllib
import re
from bs4 import BeautifulSoup
import random
import datetime


conn = pymysql.connect(host='127.0.0.1',user='root',passwd='lovol12345',charset='utf8')

cur = conn.cursor()
cur.execute("USE testMysql")


random.seed(datetime.datetime.now())

def insert_data(title,url,created):
	cur.execute("select * from pages where url=%s",(url))
	if cur.rowcount == 0:
		cur.execute("insert into pages (title,url,created) values (%s,%s,%s)",(title,url,created))
		conn.commit()
		return cur.lastrowid
	else:
		cur.fetchone()[0]


pages = set()

def get_url(url_link):
	global pages

	pattern = re.compile('^(http:\/\/money\.163\.com\/)(\d+\/)(\d+\/)(\d+\/)[A-Z0-9]+\.html')

	html = urllib.urlopen(url_link)
	bsObj = BeautifulSoup(html,"html.parser")

	
	created_at = bsObj.find("span",{"class":"time"})

	data_list = bsObj.findAll("a",href=pattern)
	for data in data_list:
		if data.attrs['href'] not in pages:
			insert_data(data.get_text(),data.attrs['href'],created_at)
			newPage = data.attrs['href']
			print newPage
			pages.add(newPage)


	
	 


get_url('http://money.163.com/special/pinglun/')
cur.close()
conn.close()




'''
url: "http://search.jd.com/Search?keyword=%E5%B9%BC%E7%8C%AB%E7%8C%AB%E7%B2%AE&enc=utf-8#filter"

print jd_search(keyword)

[dict,dict,dict]
dict {pic:'',title:'',price:'',url:''}

'''