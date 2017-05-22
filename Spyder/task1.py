#coding=utf-8

import urllib
from bs4 import BeautifulSoup

html = urllib.urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read())

name_list = bsObj.findAll("span",{"class":"green"})
for name in name_list:
	print name.get_text()