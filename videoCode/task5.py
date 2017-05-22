#coding=utf-8

'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''

def func(name):
	list_str = list(name)
	list_str[0] = list_str[0].upper()
	str_list = ''.join(list_str)
	return str_list

print func("lilei")
print func("hanmeimei")
print func("Hanmeimei")



"""
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"

"""

def func(name,type_str=None):
	#print type(type_str)
	if type == None:
		list_str = list(name)
		list_str[0] = list_str[0].upper()
		str_list = ''.join(list_str)
		return str_list
	elif type_str == 'string.lower':
		name_lower = name.lower()
		return name_lower
	else:
		name_upper = name.upper()
		return name_upper

print func("lilei")
print func("LILEI",'string.lower')
print func("lilei",'string.upper')


"""
3.定义一个func(*kargs),效果如下。
l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6

"""

def func(*kargs):
	# num_dict = {}
	# for i in range(len(kargs)):
	# 	num_dict[i] = kargs[i]
	# #return num_dict
	return kargs

l = func(5,2,3,4,5)
for i in l:
	#print i,
	print i 
#print func(5,2,3,4,5)


"""
4.定义一个func(*kargs)，该函数效果如下。

assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None

"""

def func_str(*kargs):
	str_list = []
	for i in range(len(kargs)):
		if isinstance(kargs[i],str):
			str_list.append(kargs[i])
	if str_list:
		return str_list[0]
	else:
		return None


print func_str(222,1111,'xixi','hahahah')
print func_str(7,'name','dasere')
print func_str(1,2,3,4)

# def func_str(*kargs):
# 	lis = filter(lambda x:isinstance(x,str),kargs)
# 	len_lis = [len(i) for i in lis]
# 	if len_lis:
# 		min_index = min(len_lis)
# 		return lis[len_lis.index(min_index)]
# 	return None

# print func_str(222,1111,'xixi','hahahah')
# print func_str(7,'name','dasere')
# print func_str(1,2,3,4)



"""
5.定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"

"""

def func_dict(name=None,**kwargs):
	data = []
	for k,v in kwargs.items():
		data.extend([',',str(k),':',str(v)])
	info = ''.join(data)
	return "%s%s"%(name,info)


print func_dict("lilei")
print func_dict("lilei",years=4)
print func_dict("lilei",years=10,body_weight=20)











