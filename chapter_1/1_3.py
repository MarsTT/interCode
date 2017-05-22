'''
	Query the string's all order
'''




# example1 

# import itertools

# a = "abc"

# for order in itertools.permutations(a,3):
# 	print ''.join(order)


#example2 

# def permutation(result,str,list):

# 	if len(list) == 1:
# 		result.append(str + " "+list[0])

# 	for list_str in list:
# 		list_temp = list[:]
# 		list_temp.remove(list_str)
# 		permutation(result,str+" "+list_str,list_temp)

# test = []
# permutation(test,"",['a','b','c'])
# print test


#example3

'''
	1) from the end to start,find the first element that (before < after),mark the low = 0
	2)
'''


def permutations(n):
    indices = list(range(n))
    print (indices)
    while True:
        low_index = n-1
        while low_index > 0 and indices[low_index-1] > indices[low_index]:
            low_index -= 1
        if low_index == 0:
            break
        low_index -= 1
        high_index = low_index+1
        while high_index < n and indices[high_index] > indices[low_index]:
            high_index += 1
        high_index -= 1
        indices[low_index], indices[high_index] = indices[
            high_index], indices[low_index]
        indices[low_index+1:] = reversed(indices[low_index+1:])
        print(indices)

permutations(4)






