'''
	query the brother_string
	the word contain the same char/count(str)
	not same is order
'''

a = ['abd','adb','acf','edf','cdf','df','ab','dba','dab']
b = 'abd'

for i in range(len(a)):
	a_set = set(a[i])
	if a_set == set(b):
		print a[i]
	else:
		print "no pattern!"
