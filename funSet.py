#coding=utf-8
def num_dict(str_list):
	str_dict = {}
	for i in str_list:
		if i not in str_dict:
			str_dict[i] = 1
		else:
			str_dict[i] += 1
	return str_dict



class Test(object):

	#将函数方法当内部属性
	@property
	def get_num(self):
		return 45

	#将函数当做内部静态方法，不需要实例化，即可调用
	@staticmethod
	def get_str():
		return "aa"


t = Test()
print t.get_num

print Test.get_str()

