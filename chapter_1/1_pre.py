'''
	Q1
	set the string is reverse
	example: "july" ==== "yluj"
'''


'''
	Q2
	set the string is mix('*','a-z')
	you need move the "*" to the left, move the 'a-z' to the right
'''

# import re

# a = "s*c*d***ef*"

# a_spe = re.compile('\*')
# a_spe_list = a_spe.findall(a)
# #print a_spe_list
# a_spe_str = ''.join(a_spe_list)



# a_char = re.compile('\w')
# a_char_list = a_char.findall(a)
# #print a_char_list
# a_char_str = ''.join(a_char_list)

# print "Change's result is >> {}{}".format(a_spe_str,a_char_str)

'''
	Q3
	computer the number of string's every char
'''

# a = "aAsbTamcdFKtdstsf"
# a_list = list(a)

# def str_num_dict(str_list):
# 	num_dict = {}
# 	for li in str_list:
# 		if li not in num_dict:
# 			num_dict[li] = 1
# 		else:
# 			num_dict[li] += 1

# 	return num_dict

# print str_num_dict(a_list)


'''	
	Q4
	Find the Name from the article,the Name is used the ('a-z',' ','*','?')
	'*' represent the zero or the many letters
	'?' represent the any letter
'''

# import re

# name_p = re.compile('D\w+\sYat\w+')


# f = open('1_pre.txt','r')

# content = []
# for lines in f.readlines():
# 	#print list(lines)
# 	line_str = lines.strip()
# 	if len(lines) != 0:
# 		content.append(line_str)

# for keys_id in range(len(content)):
# 	keys = name_p.findall(content[keys_id])
# 	if len(keys) != 0:
# 		print keys

# f.close()

'''
	Q5
	compression the string
	example: "abc efg hij" ==== "cba gfe jih"
'''
# import re

# a = "abc     efg hij"

# a_out = re.sub(r"\s{2,}"," ",a)
# print a_out


# a_list_split = a_out.split(' ')
# print a_list_split

# a_list_re = []
# for i in range(len(a_list_split)):
# 	a_list = list(a_list_split[i])
# 	a_list.reverse()
# 	a_list_re.append(''.join(a_list))    
# print a_list_re

# a_re = ' '.join(a_list_re)
# print a_re


'''
	Q6
	the user input the string('a-z')
	compression the string when char is replement twice or more
	example: 'xxxyyyyyyz' ==== '3x6y1z'  'adef' ==== '1a1d1f' 'ppppppp' ====== '7p'
'''
# import funSet

# a_input = raw_input('Please input the string:')

# a_input_list = list(a_input)

# a_input_dict = funSet.num_dict(a_input_list)

# #print list(a_input_dict)

# a_list = []

# for key,value in a_input_dict.items():
# 	a_list.append("%s%s"%(key,value))
# 	#print "%s%s"%(key,value)
# print a_list


'''
	Q7
	find the first and only one word_char
	example: "abaccdeff" ======= b
'''
# import funSet

# b = "abaccdeff"

# b_list = list(b)

# b_dict = funSet.num_dict(b_list)

# for key in b_dict:
# 	if b_dict[key] == 1:
# 		print key
# 		break

'''
	Q8
	delete the pattern from the string
	example: "They are students" ====== pattern("aeiou")========"Thy r stdnts"
'''

c = "They are students"

c_pattern = "aeiou"

c_split = c.split(' ')
print c_split

c_split_list = []

for i in range(len(c_split)):
	c_split_list.append(list(c_split[i]))
	
print c_split_list
c_pattern_list = list(c_pattern)
print c_pattern_list








