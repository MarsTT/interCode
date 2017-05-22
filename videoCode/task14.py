#coding=utf-8

'''
习题一：已知列表 info = [1,2,3,4,55,233]
生成6个线程对象,每次线程输出一个值，最后输出："the end"。
'''

import threading


def test(info_index):
	info = [1,2,3,4,55,333]
	print info[info_index]

#ts = []

for i in xrange(0,6):
	print "Thread%s starting\n"%i
	th = threading.Thread(target=test,args=[i])
	th.start()
	print "\n"
	print "Thread%s ending\n"%i
#	ts.append(th)

# 保证当前线程执行结束，才能执行后面的程序
# for i in ts:
# 	i.join()

print "the end"


'''
习题二：
已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 
用多线程的方式分别打开列表里的URL，并且输出对应的网页标题和内容。
'''

import threading
import urllib
from bs4 import BeautifulSoup



def url_test(url_index):
	url_info = ['http://www.sohu.com','http://www.163.com','http://www.sina.com']
	url = urllib.urlopen(url_info[url_index])
	content = url.read()
	bs4Obj = BeautifulSoup(content)
	#print bs4Obj.title.get_text()
	print bs4Obj.title

url_th = []
for i in xrange(3):
	#print "the %i url start"%i
	th = threading.Thread(target=url_test,args=[i])
	th.start()
	url_th.append(th)
	#print "the %i url end"%i
for i in url_th:
	i.join()


'''
习题三：
已知列表 urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com'] 
用多线程的方式分别打开列表里的URL，输出网页的http状态码。
'''

import threading
import urllib


def url_code(url_index):
	urlinfo = ['http://www.sohu.com','http://www.163.com','http://www.sina.com']
	url = urllib.urlopen(urlinfo[url_index])
	print url.code

url_in = []
for i in xrange(3):
	th = threading.Thread(target=url_code,args=[i])
	th.start()
	url_in.append(th)

for i in url_in:
	i.join()

#print url_code(1)


					     