def num_dict(str_list):
	str_dict = {}
	for i in str_list:
		if i not in str_dict:
			str_dict[i] = 1
		else:
			str_dict[i] += 1
	return str_dict

def combina(num_list,n):
	