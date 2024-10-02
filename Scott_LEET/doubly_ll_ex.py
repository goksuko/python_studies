class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None
		

class DoublyLinkedList:
	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length = 1

	def print_list(self):
		temp = self.head
		while temp is not None:
			print(temp.value)
			temp = temp.next
		
	def append(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node
		self.length += 1
		return True

	def swap_first_last(self):
		if self.length <= 1:
			return
		first = self.head
		last = self.tail
		temp = last
		last.prev.next = first
		last.prev = None
		last.next = first.next
		self.head = last
		first.prev = temp.prev
		first.next.prev = temp
		first.next = None
		self.tail = first
	
	# def reverse(self): #not enough for reverse_next_and_prev_pointers_test
	# 	if self.length <= 1:
	# 		return
	# 	first = self.head
	# 	last = self.tail
	# 	before = self.head
	# 	temp = before.next
	# 	before.next = None
	# 	while temp:
	# 		after = temp.next
	# 		temp.next = before
	# 		temp.rev = after
	# 		before = temp
	# 		temp = after
	# 	self.head = last
	# 	self.tail = first

	def reverse(self):
		temp = self.head
		while temp is not None:
			# swap the prev and next pointers of node points to
			temp.prev, temp.next = temp.next, temp.prev
			
			# move to the next node
			temp = temp.prev
			
		# swap the head and tail pointers
		self.head, self.tail = self.tail, self.head

	def is_palindrome(self):
		first = self.head
		last = self.tail
		half = int(self.length / 2)
		for _ in range(half):
			if first.value != last.value:
				return False
			first = first.next
			last = last.prev
		return True
	
	def swap_pairs(self): #my_solution
		if self.length <= 1:
			return
		before = self.head
		future_head = before.next
		half = int(self.length / 2)
		for _ in range(half):
			temp = before.next
			after = temp.next
			if after and after.next:
				before.next = after.next
				after.prev = before
			elif after and not after.next:
				before.next = after
				after.prev = before
			elif not after:
				before.next = None
			temp.prev = before.prev
			before.prev = temp
			temp.next = before
			before = after

		self.head = future_head
		return self.head

	def swap_pairs_2(self): #course solution
		dummy_node = Node(0)
		dummy_node.next = self.head
		previous_node = dummy_node
	
		while self.head and self.head.next:
			first_node = self.head
			second_node = self.head.next
	
			previous_node.next = second_node
			first_node.next = second_node.next
			second_node.next = first_node
	
			second_node.prev = previous_node
			first_node.prev = second_node
	
			if first_node.next:
				first_node.next.prev = first_node
	
			self.head = first_node.next
			previous_node = first_node
	
		self.head = dummy_node.next
	
		if self.head:
			self.head.prev = None

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)


print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.swap_first_last()


print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()



"""
	EXPECTED OUTPUT:
	----------------
	DLL before swap_first_last():
	1
	2
	3
	4

	DLL after swap_first_last():
	4
	2
	3
	1

"""

