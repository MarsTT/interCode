#coding=utf-8

'''
定义一个列表的操作类：Listinfo

包括的方法: 

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key() 

list_info = Listinfo([44,222,111,333,454,'sss','333'])
'''
class ListInfo(object):

	def __init__(self,list_args):
		self.list_args = list_args

	def add_key(self,keyname):
		new_list = self.list_args
		new_list.append(keyname)
		return new_list

	def get_key(self,num):
		new_list = self.list_args
		if isinstance(num,int):
			for i in range(len(new_list)):
				if num == new_list[i]:
					return "Find it!"
				else:
					return "Not Found!"
		else:
			return "Data Type is error!"

	def update_list(self,list_new):
		new_list = self.list_args
		#for i in range(len(list_new)):
		new_list.extend(list_new)

		return new_list

	def del_key(self):
		new_list = self.list_args
		del new_list[len(new_list)-1]
		return new_list


li = ListInfo([44,222,111,333,454,'sss','333'])
print li.add_key(9),li.add_key('b')
print li.get_key(44),li.get_key('abc'),li.get_key(888)
print li.update_list([71,93,'asasa'])
print li.del_key()


'''
定义一个集合的操作类：Setinfo

包括的方法: 

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)
'''

class SetInfo(object):

	def __init__(self,set_args):
		self.set_args = set_args

	def add_setinfo(self,keyname):
		new_set = self.set_args
		new_set.add(keyname)
		return new_set

	def get_intersection(self,unioninfo):
		new_set = self.set_args

		#以下代码分别求两个集合的交集，并集，差集
		#uni_set = new_set & unioninfo
		#uni_set = new_set | unioninfo
		uni_set = new_set - unioninfo
		return uni_set


si_set = set([1,2,4,7,22])
si = SetInfo(si_set)
print si.add_setinfo('ttaa')
print si.get_intersection(set([2,4,8,11,90]))





















