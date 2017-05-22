
'''
	Q1: exist the string a = "i,love,python"
		find the substring "love"
'''

# a = "i,love,python"
# a_list = a.split(',')
# print a_list[1]


'''
	Q2: exist the string a = "aabbccddee"
		make the "dd" exchange the "ff"
'''

# a = "aabbccddee"

# b = a.replace(a[6:8],'ff')

# print b


'''
	Q3:a = "ab2b3n5n2n67mm4n2"
	1) re ==> digits
	2) count('n')
	3) count() ===== every_word ===== dict
'''
import re

a = "ab2b3n5n2n67mm4n2"

p_digits = re.compile(r"\d")
#print (p.findall(a))

p_digits_temp = p_digits.findall(a)
print p_digits_temp


p_n = re.compile(r'n')
p_n_temp = p_n.findall(a)
#print p_n_temp

p_str = re.compile(r'\D')
p_str_temp = p_str.findall(a)
print p_str_temp	

def dict_product(listStr):
	p_dict = {}
	count = 1
	for n_i in listStr:
		if n_i not in p_dict:
			p_dict[n_i] = count
		else:
			p_dict[n_i] += 1

	print p_dict


dict_product(p_str_temp)



