import urllib
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())

#匹配以/wiki/开头的网址
pattern = re.compile("^(/wiki/)((?!:).)*$")

def get_links(articleUrl):
	html = urllib.urlopen("http://en.wikipedia.org"+articleUrl)
	bs_html = BeautifulSoup(html,"html.parser")
	#找到所有url对应的网址
	return bs_html.find("div",{"id":"bodyContent"}).findAll("a",href=pattern)

links = get_links("/wiki/Kevin_Bacon")

while len(links) > 0:
	# 随机选择链接网址的一个，然后提取属性为"href"的网址
	new_article = links[random.randint(0,len(links)-1)].attrs["href"]
	print new_article
	#递归调用链接
	links = get_links(new_article)