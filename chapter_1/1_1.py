'''
	the string is / not is contain
'''


a = 'ABCD'
#b = 'BAD'
#b = 'BCE'
b = 'AA'

a_set = set(a)
b_set = set(b)



c_set = a_set & b_set

if c_set == b_set:
	print "True"
else:
	print "False"

# print a_set
# print b_set
# print c_set