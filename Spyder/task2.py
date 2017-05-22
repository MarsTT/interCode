#coding=utf-8


#from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup

html = urllib.urlopen("http://www.pythonscraping.com/pages/page3.html")

# content = html.read()
# print content

# 找到table标签下的子标签,注意区分后代标签
bsObj = BeautifulSoup(html,"html.parser")
for child in bsObj.find("table",{"id":"giftList"}).children:
	print child

# 找到tr的兄弟标签
# bsObj_next = BeautifulSoup(html,"html.parser")
# for sibling in bsObj_next.find("table",{"id":"giftList"}).tr.next_siblings:
# 	print sibling