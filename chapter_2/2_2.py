'''
	input the integer(n) ,find the pair and this pair's add is the input integer(1)
	example: [1,2,4,5,7,11,15]   /    15 =========   4+11 = 15 ======  output:[4,11]
'''

from itertools import product
from itertools import combinations

a_input = []

for i in range(7):
	a_input.append(int(raw_input("Please input the num%d:" % (i+1))))

#print a_input

#print list(product(a_input,a_input))
#print list(product(a_input,repeat = 4))

print list(combinations(a_input,2))