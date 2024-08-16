def insertion_sort(the_list):
	length = len(the_list)
	if length <= 1:
		return the_list
	index = 1
	while index < length:
		copy = index
		while the_list[index] < the_list[index - 1] and index > 0:
			temp = the_list[index]
			the_list[index] = the_list[index - 1]
			the_list[index - 1] = temp
			index -= 1
		index = copy + 1
	return the_list

print(insertion_sort([4,2,6,5,1,3]))



"""
	EXPECTED OUTPUT:
	----------------
	[1, 2, 3, 4, 5, 6]
	
 """

