#coding=utf-8

'''
	define a function,find the max and min num
'''
# def func(*num):
# 	#print type(num)
# 	num_list = []
# 	for i in range(len(num)):
# 		num_list.append(num[i])
# 	num_list.sort()
# 	return "the min num is {min},the max num is {max}".format(
# 		min=num_list[0],max=num_list[len(num_list)-1])


# print func(3,2,1,9,3,2,5,0,2,32,1,2,332,1)

'''
	define a function,find the max_length str
'''

# def func(*str):
# 	str_list = []
# 	for i in range(len(str)):
# 		str_list.append(str[i])

# 	for i in range(len(str_list)-1):
# 		if len(str_list[i]) > len(str_list[i+1]):
# 			str_list[i],str_list[i+1] = str_list[i+1],str_list[i]
	
# 	return "the max_length is:%s"%(str_list[len(str_list)-1])


# print func('as','sasas','ewsaasdr','sartaseyssyysysysy','sydyahsge')


'''
	定义一个方法get_doc(module)，
	module参数为该脚本中导入或定义的模块对象，
	该函数返回module的帮助文档。
'''

import os
def get_doc(module):
	a = 'pydoc %s'% module
	m = os.popen(a).read()
	return m



#import os
def get_text(f):
	a = 'cat %s'% f
	m = os.popen(a).read()
	return m


import glob
def get_dir(folder):
	a = "%s/*.*"% folder
	temp = glob.glob(a)
	if temp == []:
		return "the folder is not null"
	else:
		return temp








