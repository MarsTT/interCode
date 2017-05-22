#coding=utf-8

'''
习题一：
 
1.1 用time模块获取当前的时间戳.
1.2 用datetime获取当前的日期，例如：2013-03-29
1.3 用datetime返回一个月前的日期：比如今天是2013-3-29 一个月前的话：2013-02-27
'''

import time

from datetime import date
from datetime import datetime
from datetime import timedelta

#from datetime import *



print time.time()

print date.today()
#print date.weekday(date.today())

old_date = date.today() - timedelta(days=30)
print old_date


now = datetime.now()
print now

print time.localtime()




'''
习题二:
1 用os模块的方法完成ping www.baidu.com 操作。
2 定义一个函数kouzhang(dirpwd)，用os模块的相关方法，
返回一个列表，列表包括：dirpwd路径下所有文件不重复的扩展名，
如果有2个".py"的扩展名，则返回一个".py"。
'''

import os

def kouzhang(dirpwd):

	file_list = []
	if not os.path.exists(dirpwd):
		return "not exist!"

	for f in os.listdir(dirpwd):
		file_path = os.path.join(dirpwd,f)
		file_list.append(file_path)
	return file_list

print kouzhang('/Users/marxia/Desktop/test_folder')




'''
习题三：

定义一个函数xulie(dirname,info) 
参数：dirname:路径名，info:需要序列化的数据，
功能：将info数据序列化存储到dirname路径下随机的文件里。  
'''