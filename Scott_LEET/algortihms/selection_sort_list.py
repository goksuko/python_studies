def selection_sort(the_list):
	length = len(the_list)
	j = 0
	while j < length: 
		min_index = j
		i = j
		while i < length:
			if the_list[i] < the_list[min_index]:
				min_index = i
			i += 1
		if j != min_index:
			temp = the_list[min_index]
			the_list[min_index] = the_list[j]
			the_list[j] = temp
		j += 1
	return the_list






print(selection_sort([4,2,6,5,1,3]))


 
"""
	EXPECTED OUTPUT:
	----------------
	[1, 2, 3, 4, 5, 6]
	
 """

