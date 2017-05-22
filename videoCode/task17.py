#coding=utf-8

'''
1 已知字符串:
info = '<a href="http://www.baidu.com">baidu</a>'

用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"
'''

import re


# 
info = '<a href="http://www.baidu.com">baidu</a>'

#pattern = '"(\w+):\/\/([^/:]+)"'
pattern_url = '"(\w+):\/\/(\w+)\.(\w+)\.(\w+)"'

#pattern_url = r'\d'
url_search = re.search(pattern_url,info)

if url_search:
	print url_search.group()
else:
	print "search failure!"

'''
2 字符串："one1two2three3four4" 用正则处理，输出 "1234"
'''

import re

str_info = "7one1two8three9four4"
pattern_num = re.compile(r'\d+')
print re.findall(pattern_num,str_info)

# pattern_num = '(\d)\w+(\d)\w+(\d)\w+(\d)'

# num_search = re.search(pattern_num,str_info)
# num_list = []

# # if num_search:
# # 	print num_search.group(3)

# if num_search:
# 	for i in range(1,5):
# 		num_list.append(num_search.group(i))
# print ''.join(num_list)

print re.split(r'[a-z]+',str_info)


'''
3 已知字符串：
text = "JGood is a handsome boy, he is cool, clever, and so on..." 
查找所有包含'oo'的单词。
'''



'''
4 为什么在unix里，grep后面的正则有些时候要加引号，有些时候不需要。
'''