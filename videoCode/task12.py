#coding=utf-8

'''
1 定义一个函数func(filename) 
filename:为文件名，
用with实现打开文件，并且输出文件内容。
'''
import os

def func(filename):
	try:
		with open(filename,'r') as file:		
			content = file.read()
		return content
	except IOError:
		return "no exist file"

print func(os.path.join(os.getcwd(),'task.py'))

'''
2 定好一个函数func(listinfo) 
listinfo:为列表，
listinfo=[133,88,33,22,44,11,44,55,33,22,11,11,444,66,555] 
返回一个列表包含小于100的偶数，并且用assert来断言
返回结果和类型。
'''


def func_odd(listinfo):
	new_list = []
	for i in range(len(listinfo)):
		if listinfo[i] % 2 == 0:
			new_list.append(listinfo[i])

	return new_list

print func_odd([133,88,33,22,44,11,44,55,33,22,11,11,444,66,555])
# assert 表达式,"出错以后抛出的信息"
assert func_odd([133,88,33,22,44,11,44,55,33,22,11,11,444,66,555])==[88,22,44,44,22,444,66],"you are wrong"



'''
3 自己定义一个异常类，
继承Exception类, 
捕获下面的过程：
判断raw_input()输入的字符串长度是否小于5，
如果小于5，
比如输入长度为3则输出:
" The input is of length 3,expecting at least 5'，
大于5输出"print success'
'''


class myException(Exception):

	# def __init__(self,error,msg):
	# 	self.args = (error,msg)
	# 	self.error = error
	# 	self.msg = msg

	# def get_input(self,input_data):
	# 	if len(input_data) < 5:
	# 		return "the input is of length is %s,excepting at least is 5" % len(input_data)
	# 	else:
	# 		return "print success"


	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length = length
		self.atleast = atleast


try:
	input_data = raw_input("Please input the string:")
	if len(input_data) < 5:
		raise myException(len(input_data),5)
	else:
		print "print success"
except myException as e:
	print "the input is of length %s ,excepting at least is 5" % e.length
else:
	print "No exception was raised"




