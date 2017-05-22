'''	
	dicision the string is equaling string.reverse()
'''


a = 'madam'

a_list = list(a)
#print a_list 

a_list.reverse()

a_reverse = ''.join(a_list)
print a_reverse


'''
	tips: "is" is compare the quotes
		  "==" is compare the content
'''

if a == a_reverse:
	print "this is the HuiWen"
else:
	print "this is not the HuiWen"