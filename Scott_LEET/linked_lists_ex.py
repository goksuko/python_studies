class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		

class LinkedList:
	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node

		
	def append(self, value):
		new_node = Node(value)
		if self.head == None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
		return True
		

	def find_middle_node(self):
		slow = self.head
		fast = self.head
		while fast is not None and fast.next is not None:
			slow = slow.next
			fast = fast.next.next
		return slow
	
	def has_loop(self):
		slow = self.head
		fast = self.head
		while fast is not None and fast.next is not None:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True
		return False
	
	def partition_list(self, x):
		if self.head == None:
			return None
		dummy1 = Node(0)
		dummy2 = Node(0)
		temp = self.head
		prev1 = dummy1
		prev2 = dummy2
		for _ in range(self.length):
			if temp.value >= x:
				prev1.next = temp
				prev1 = temp
				temp = temp.next
				prev1.next = None
			else:
				prev2.next = temp
				prev2 = temp
				temp = temp.next
				prev2.next = None
		prev2.next = dummy1.next
		self.head = dummy2.next
		dummy1.next = None
		dummy2.next = None
		return self.head

	def remove_duplicates(self):
		if self.head is None:
			return None
		values = set()
		prev = self.head
		values.add(prev.value)
		temp = prev.next
		while temp:
			if temp.value in values:
				prev.next = temp.next
				self.length -= 1
			else:
				values.add(temp.value)
				prev = temp
			temp = temp.next
		return self.head
	
	# def binary_to_decimal(self):
	# 	temp = self.head
	# 	power = self.length
	# 	nb = 0
	# 	while temp:
	# 		copy = power
	# 		times = 1
	# 		for _ in range(copy - 1):
	# 			times *= 2
	# 		nb += times * temp.value
	# 		power -= 1
	# 		temp = temp.next
	# 	return nb

	def binary_to_decimal(self):
		temp = self.head
		nb = 0
		while temp:
			nb = nb * 2 + temp.value
			temp = temp.next
		return nb
	
	def reverse_between(self, start_index, end_index):
		if self.length <= 1:
			return
		dummy = Node(0)
		dummy.next = self.head
		prev = dummy
		for _ in range(start_index):
			prev = prev.next
		temp = prev.next
		for _ in range(end_index - start_index):
			after = temp.next
			temp.next = after.next
			after.next = prev.next
			prev.next = after
		self.head = dummy.next

# def find_length(my_linked_list):
# 	i = 0
# 	temp = my_linked_list.head
# 	while temp is not None:
# 		temp = temp.next
# 		i += 1
# 	return i
		
def find_kth_from_end(my_linked_list, k):
	slow = my_linked_list.head
	fast = my_linked_list.head
	for _ in range(k):
		if fast is None:
			return None
		fast = fast.next
	while fast is not None:
		slow = slow.next
		fast = fast.next
	return slow

	# def partition_list(self, x):
	# 	if self.length == 0 or self.length == 1:
	# 		return self.head
	# 	tail = self.head
	# 	while tail.next is not None:
	# 		tail = tail.next
	# 	temp = self.head
	# 	before = Node(0)
	# 	before.next = self.head
	# 	self.head = before
	# 	self.length += 1
	# 	for _ in range(self.length - 1):
	# 		if temp.value >= x:
	# 			after = temp.next
	# 			tail.next = temp
	# 			tail = temp
	# 			temp.next = None
	# 			before.next = after
	# 			temp = after
	# 		else:
	# 			before.next = temp
	# 			temp =temp.next
	# 			before = before.next
	# 	head = self.head
	# 	self.head = head.next
	# 	self.length -= 1
	# 	return self.head


	
	
