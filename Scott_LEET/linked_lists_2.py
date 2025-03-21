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
		return True
	
	def pop(self):
		if self.length == 0:
			return None
		temp = self.head
		pre = self.head
		while temp.next:
			pre = temp
			temp = temp.next
		self.tail = pre
		self.tail.next = None
		self.length -= 1
		if self.length == 0:
			self.head = None
			self.tail = None
		return temp
			

	def prepend(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			new_node.next = self.head
			self.head = new_node
		self.length += 1
		return True
	
	def pop_first(self):
		if self.length == 0:
			return None
		temp = self.head
		self.head = self.head.next
		temp.next = None
		self.length -= 1
		if self.length == 0:
			self.tail = None
		return temp

	def get(self, index):
		if index < 0 or index >= self.length:
			return None
		temp = self.head
		for _ in range(index):
			temp = temp.next
		return temp
	
	def set_value(self, index, value):
		temp = self.get(index)
		if temp:
			temp.value = value

	def insert(self, index, value):
		if index < 0 or index >= self.length:
			return False
		elif index == 0:
			return self.prepend(value)
		elif index == self.length:
			return self.append(value)
		temp = self.get(index - 1)
		new_node = Node(value)
		new_node.next = temp.next
		temp.next = new_node
		self.length += 1
		return True
	
	def remove(self, index):
		if index < 0 or index >= self.length:
			return None
		elif index == 0:
			return self.pop_first()
		elif index == self.length - 1:
			return self.pop()
		pre = self.get(index - 1)
		temp = pre.next
		pre.next = temp.next
		temp.next = None
		self.length -= 1
		return temp		
	
	def reverse(self):
		if self.length < 0:
			return False
		elif self.length <= 1:
			return True
		temp = self.head
		self.head = self.tail
		self.tail = temp
		after = temp.next
		before = None
		for _ in range(self.length):
			after = temp.next
			temp.next = before
			before = temp
			temp = after
		return True


	# def append_in_btw(self, index, value):
	# 	if index < 0 or index > self.length:
	# 		return None
	# 	elif index == 0:
	# 		self.prepend(value)
	# 		return self.head
	# 	elif index == self.length:
	# 		self.append(value)
	# 		return self.head
	# 	else:
	# 		new_node = Node(value)
	# 		pre = self.head
	# 		for _ in range(index - 1):
	# 			pre = pre.next
	# 		new_node.next = pre.next
	# 		pre.next = new_node
	# 		return self.head
		
		


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.prepend(0)

my_linked_list.print_list()

print("popped first")
my_linked_list.pop_first()
my_linked_list.print_list()

print("popped first")
my_linked_list.pop_first()
my_linked_list.print_list()

print("popped first")
my_linked_list.pop_first()
my_linked_list.print_list()

print("popped first")
my_linked_list.pop_first()
my_linked_list.print_list()

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.prepend(0)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

my_linked_list.print_list()
print(my_linked_list.get(3))
print(my_linked_list.get(7))
print(my_linked_list.get(-3))

my_linked_list.set_value(3, 5)
my_linked_list.print_list()
my_linked_list.set_value(3, 3)

my_linked_list.insert(0, -1)
my_linked_list.insert(-1, -2)
my_linked_list.insert(8, 8)
my_linked_list.print_list()

my_linked_list.remove(2)
my_linked_list.print_list()
my_linked_list.pop_first()
my_linked_list.insert(1,1)
my_linked_list.print_list()

my_linked_list.reverse()
my_linked_list.print_list()
