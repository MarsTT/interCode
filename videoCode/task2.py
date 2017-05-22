#coding=utf-8
'''
	define the function 'get_num(num)'
	num is the digits
'''

def get_num(num):
	num_list = []
	for i in range(len(num)):
		if isinstance(num[i],int):
			if num[i]%2 == 0:
				num_list.append(num[i])
		else:
			return "error : the element is not integer"
	return num_list
print get_num([1,2,4,6,7,9])

assert get_num([1,2,4,5,7,9]) == [2,4]



'''
	define function 'func'
	func can import any more args,return the max element
'''


# def func(*num):
# 	num_list = list(num)
# 	#return num
# 	max_num = []
# 	for i in range(len(num_list)):
# 		for j in range(len(num_list[i])-1):
# 			if num_list[i][j] > num_list[i][j+1]:
# 				num_list[i][j+1],num_list[i][j] = num_list[i][j],num_list[i][j+1]
# 				max_num.append(num_list[len(num_list)-1])
# 	return max_num


# print func([1,2],[7,3],[2,5],[8,9],[2,6])