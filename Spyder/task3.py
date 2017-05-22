#coding=utf-8


import urllib
from bs4 import BeautifulSoup
import re

html = urllib.urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
# content = html.read()
# print content
bsObj = BeautifulSoup(html.read())

# link_list = bsObj.findAll('a')
# print link_list[10].attrs

# for link in bsObj.findAll('a'):
# 	if 'href' in link.attrs:
# 		print link.attrs['href']

pattern = re.compile("^(/wiki/)((?!:).)*$")

for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=pattern):
	if 'href' in link.attrs:
		print link.attrs['href']