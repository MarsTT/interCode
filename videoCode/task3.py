#coding=utf-8


'''
	定义一个方法get_fundoc(func),
	func参数为任意一个函数对象，返回该函数对象的描述文档，
	如果该函数没有描述文档，则返回"not found"
'''

def get_fundoc(func):
	'''
		实现描述文档
	'''
	if func.__doc__ == "":
		return "not found"
	else:
		print func.__doc__

'''
	测试函数
'''
def testFun():
	'''
		单纯的测试一下
	'''
	pass

get_fundoc(testFun)


'''
	定义一个方法get_cjsum(),
	求1-100范围内的所有整数的平方和。
	返回结果为整数类型。
'''

def get_cjsum():
	sum = 0
	for i in range(1,101):
		sum += i*i
	print sum
	return sum

get_cjsum()


'''
	定义一个方法list_info(list), 
	参数list为列表对象，
	怎么保证在函数里对列表list进行一些相关的操作，
	不会影响到原来列表的元素值
'''

def list_info(list):
	#if isinstance(list,list)

	'''
		注意区分下列两种复制，第一行是增加对列表的引用，结果还是对原列表进行操作
		第二行是将列表的元素复制给另一个列表，两个列表的引用不一样
	'''
	#list_new = list
	list_new = list[:]

	list_new[len(list)-1] = 5

	return list_new

a = [1,2,3]
print list_info(a)
print a

'''
	定义一个方法get_funcname(func),
	func参数为任意一个函数对象，需要判断函数是否可以调用，
	如果可以调用则返回该函数名(类型为str)，否则返回 “fun is not function"。
'''



