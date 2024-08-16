class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		

class LinkedList:
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
			self.tail = new_node
		self.length += 1
	
	def swap_value(self, i, j):
		if i < j:
			small = i
			big = j
		else:
			small = j
			big = i
		if big >= self.length:
			return False
		temp = self.head
		for _ in range(small):
			temp = temp.next
		first = temp
		for _ in range(big - small):
			temp = temp.next
		second = temp
		nb = first.value
		first.value = second.value
		second.value = nb
		return True

	# def bubble_sort(self): #mine
	# 	for _ in range(self.length - 1):
	# 		temp = self.head
	# 		while temp.next:
	# 			if temp.value > temp.next.value:
	# 				nb = temp.value
	# 				temp.value = temp.next.value
	# 				temp.next.value = nb
	# 			temp = temp.next

	def bubble_sort(self):
		if self.length < 2:
			return
		
		sorted_until = None
		
		while sorted_until != self.head.next:
			current = self.head
			while current.next != sorted_until:
				next_node = current.next
				if current.value > next_node.value:
					current.value, next_node.value = next_node.value, current.value
				current = current.next
			sorted_until = current

my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
	EXPECTED OUTPUT:
	----------------
	Linked List Before Sort:
	4
	2
	6
	5
	1
	3

	Sorted Linked List:
	1
	2
	3
	4
	5
	6

"""

