def bubble_sort(the_list):
	length = len(the_list)
	j = 0
	while j < length - 1:
		i = 0
		while i < length - 1:
			
			if the_list[i] > the_list[i + 1]:
				temp = the_list[i]
				the_list[i] = the_list[i + 1]
				the_list[i + 1] = temp
			i += 1
		j += 1

	return the_list





print(bubble_sort([4,2,6,5,1,3]))

 

"""
	EXPECTED OUTPUT:
	----------------
	[1, 2, 3, 4, 5, 6]
 """