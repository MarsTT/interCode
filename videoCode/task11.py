#coding=utf-8


'''
1 定义一个函数func(filename) 
filename:文件的路径，
函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。
'''

def func(filename):

	try:
		f = open(filename,'r')
	except IOError:
		print "文件路径有错!"
	else:
		content = f.read()
		print content
		f.close()
	finally:
		print "文件操作结束!"
		

	#return None
	# f = open(filename,'r')
	# content = f.read()
	# f.close()

func("/Users/marxia/Desktop/interCode/funSet.py")

func("sas") 

'''
2 定义一个函数func(urllist)  
 urllist:为URL的列表，
 例如：['http://xx.com','http://www.xx.com','http://www.xxx.com'...] 
函数功能：要求依次打开url，
打印url对应的内容，如果有的url打不开，
则把url记录到日志文件里，并且跳过继续访问下个url。
'''
import urllib
import logging
import sys

logger = logging.getLogger()
logfile = 'test.log'
hdlr = logging.FileHandler('/Users/marxia/Desktop/interCode/log/test.txt')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.NOTSET)


# try:
# 	1/0
# except:
# 	exc = sys.exc_info()
# 	logging.debug(exc[1])



def func_url(urllist):

	for i in range(len(urllist)):
		try:
			file = urllib.urlopen(urllist[i])
		except IOError:
			print "url is wrong"
			# exc = sys.exc_info()
			# print exc
			# logging.debug(exc[1])
		else:
			content = file.read()
			print content
		finally:
			file.close()


func_url(['http://www.xiatianci.com','https://github.com/MarsTT'])

'''
3 定义一个函数func(domainlist)  
 domainlist:为域名列表，
 例如：['xx.com','www.xx.com','www.xxx.com'...]
函数功能：要求依次ping 域名，
如果ping 域名返回结果为：request time out，
则把域名记录到日志文件里，并且跳过继续ping下个域名。（提示用os模块的相关方法）
'''