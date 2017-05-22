#coding=utf-8


'''
1 用lambda和filter完成下面功能：输出一个列表，列表里面包括：1-100内的所有偶数。(提示：可以用filter,lambda)
'''

a = filter(lambda x: x % 2 == 0,xrange(1,101))
print a



'''
2 用位置匹配，关键字匹配，收集匹配(元组收集,字典收集)分别写4个函数，完成功能；

传递3个列表参数：

[1,2,3],[1,5,65],[33,445,22]

返回这3个列表中元素最大的那个，结果是：445
'''


def Position(arg1,arg2,arg3):
	list_num = []
	# for i in range(3):
	# 	list_num.extend(arg[i])
	list_num.extend(arg1)
	list_num.extend(arg2)
	list_num.extend(arg3)

	#list_set = set(list_num)
	list_num.sort()
	return list_num[len(list_num)-1]

print Position([1,2,3],[1,5,65],[33,445,22])

def KV(arg1=None,arg2='',arg3=''):
	list_num = []
	# for i in range(3):
	# 	list_num.extend(arg[i])
	list_num.extend(arg1)
	list_num.extend(arg2)
	list_num.extend(arg3)

	#list_set = set(list_num)
	list_num.sort()
	return list_num[len(list_num)-1]

print KV(arg1=[1,5,65],arg2=[33,445,22],arg3=[1,2,3])

def Collect_tuple(*kargs,**kwargs):
	list_kargs = list(kargs)
	list_num = []
	for i in range(3):
		list_num.extend(list_kargs[i])
	list_num.sort()
	return list_num[len(list_num)-1]
	#return kwargs

print Collect_tuple([1,2,3],[1,5,65],[33,445,22],a=12,b=33)

def Collect_dict(**kwargs):
	#kwargs.values()
	list_num = []
	for i in range(3):
		list_num.extend(kwargs.values()[i])
	list_num.sort()
	return list_num[len(list_num)-1]

print Collect_dict(a=[1,2,3],b=[1,5,65],c=[33,445,22])







