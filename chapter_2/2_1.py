'''
	input the n integers and find the min(k)
'''

a_list = []
for i in range(7):
	a_input = int(raw_input("Please input the num%d:"%(i+1)))
	a_list.append(a_input)
print a_list
a_list.sort()
print a_list

k = 3
a_k = []
for i in range(k):
	a_k.append(a_list[i])
print a_k

#print type(a_input)
