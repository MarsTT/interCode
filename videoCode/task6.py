#coding=utf-8
'''
一：定义一个学生类。有下面的类属性：

1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int


写好类以后，可以定义2个同学测试下:

zm = student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100

lq = student('liqiang',23,[82,60,99])

返回结果：
liqiang
23
99
'''
class Student(object):

	def __init__(self,name,age,grade):
		self.name = name
		self.age = age
		self.grade = grade

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def get_course(self):
		list_course = self.grade
		list_course.sort()
		return list_course[len(list_course)-1]


zm = Student('zhangming',20,[69,88,100])
print zm.get_name(),zm.get_age(),zm.get_course()

lq = Student('liqing',23,[82,60,99])
print lq.get_name(),lq.get_age(),lq.get_course()



'''
二：定义一个字典类：dictclass。完成下面的功能：


dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)


2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})
'''

class DictClass(object):

	def __init__(self,**dict_data):
		self.dict_data = dict_data

	def del_dict(self,index):
		dict_new = self.dict_data
		dict_list_key = dict_new.keys()
		dict_list_key.remove(index)
		return dict_list_key

	def get_dict(self,kw):
		dict_new = self.dict_data
		for k,v in dict_new.items():
			#return k,v
			if kw == k:
				return v
			else:
				return "not found!"

	def get_key(self):
		dict_list = self.dict_data
		dict_list_key = dict_list.keys()
		return dict_list_key

	def update_dict(self,**kwargs):
		dict_new = self.dict_data
		new_dict = {}
		dict_key = dict_new.keys()
		dict_value = dict_new.values()

		for k,v in kwargs.items():
			dict_key.append(k)
			dict_value.append(v)

		#zip是将两个序列打包成元组
		#然后用dict将元组转化成字典
		new_dict = dict(zip(dict_key,dict_value))

		return new_dict
		#return dict_new

dc = DictClass(a=3,b=11,c=25)
print dc.del_dict('c')
print dc.get_dict('a'),dc.get_dict('e')
print dc.get_key()
print dc.update_dict(d=12,e=15)




