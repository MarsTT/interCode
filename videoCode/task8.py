#encoding=utf-8

import urllib
import random
import os

def save_url_content(url,folder_path=None):##习题1
	if not ( url.startswith('http://') or url.startswith('https://') ):
		return u'url地址不符合规格'
	if not os.path.isdir(folder_path):
		return u'folder_path非文件夹'
	d = urllib.urlopen(url)
	content = d.read()

	#随机生成一个文件
	rand_filename = 'test_%s'%random.randint(1,1000)
	#将随机生成的文件添加到文件夹中
	file_path = os.path.join(folder_path,rand_filename)
	#print file_path

	d = open(file_path,'w')
	d.write(content)
	d.close()
	return file_path

print save_url_content('https://www.cnblogs.com/yyxayz/p/4044529.html',folder_path='/Users/marxia/Desktop/test_folder')


def get_url_count(url):##习题3
	if not ( url.startswith('http://') or url.startswith('https://') ):
		return u'url地址不符合规格'
	d = urllib.urlopen(url)
	content = d.read()
	return len(content.split('<a href=')) - 1
	#return content



print get_url_count('https://www.cnblogs.com/yyxayz/p/4044529.html')


import os
#使用递归去解决
def merge(folder_path):##习题2

	if not os.path.exists(folder_path):
		return 'not exists'

	for f in os.listdir(folder_path):
		file_path = os.path.join(folder_path,f)
		if os.path.isdir(file_path):
			merge(file_path)
		else:
			merge_file = open('/Users/marxia/Desktop/merge_test','ab+')
			content = open(file_path,'r').read()
			merge_file.write(content)
			merge_file.close()

#merge('/tmp/5')
#merge('/Users/marxia/Desktop/test_folder')

import urlparse

def qs(url):##习题4
	query = urlparse.urlparse(url).query
	return dict([(k,v[0]) for k,v in urlparse.parse_qs(query).items()])

print qs('http://126.com')
print qs('http://api/api?f=5&g=6&y=5')
print qs('http://api/api?11=53')

#使用递归去解决
def delete(folder_path):##习题5
	if not os.path.exists(folder_path):
		return 'not exists'

	for f in os.listdir(folder_path):
		file_path = os.path.join(folder_path,f)
		if os.path.isdir(file_path):
			delete(file_path)
		else:
			os.remove(file_path)

#delete('/tmp/5')