#coding=utf-8


import urllib
from bs4 import BeautifulSoup
import os
import sys


def text_url(url_site,file_name):
	html = urllib.urlopen(url_site)
	bsOjb = BeautifulSoup(html,'html.parser')
	text_list = bsOjb.findAll("a")
	f = open(file_name,'w')
	for text in text_list:
		reload(sys)
		sys.setdefaultencoding('utf-8')
		f.write(text.get_text())
		f.write("\n")
		f.write("==============\n")
	f.close()

text_url("http://www.news.cn/",os.path.join(os.getcwd(),'test_ch.txt'))
text_url("http://xizang.news.cn/",os.path.join(os.getcwd(),'test_xz.txt'))




