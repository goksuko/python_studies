class Node:
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None
	
class DoublyLinkedList:
	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length = 1

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.value)
			temp = temp.next

	def append(self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			self.length = 1
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.length += 1
		self.tail = new_node

	def pop(self):
		if self.length == 0:
			return None
		temp = self.tail
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			before = self.tail.prev
			before.next = None
			self.tail = before
		self.length -= 1
		return temp

	def prepend(self, value):
		new_node = Node(value)
		if self.length == 0:
			self.tail = new_node
		else:			
			self.head.prev = new_node
			new_node.next = self.head
		self.head = new_node
		self.length += 1

	def pop_first(self):
		if self.length == 0:
			return None
		temp = self.head
		if self.length == 1:
			self.head = None
			self.tail = None
		else:
			self.head = self.head.next
			self.head.prev = None
		temp.next = None
		self.length -= 1
		return temp
	
	def get(self, index):
		if index < 0 or index >= self.length:
			return None
		if index > self.length / 2:
			rest = self.length - index
			temp = self.tail
			for _ in range(rest - 1):
				temp = temp.prev
		else:
			temp = self.head
			for _ in range(index):
				temp = temp.next
		return temp
	
	def set_value(self, index, value):
		temp = self.get(index)
		if temp:
			temp.value = value
			return True
		return False
	
	def insert(self, index, value):
		if index < 0 or index > self.length:
			return False
		if self.length == 0 or index == self.length:
			return self.append(value)
		if index == 0:
			return self.prepend(value)
		new_node = Node(value)
		before = self.get(index - 1)
		after = before.next
		before.next = new_node
		new_node.next = after
		new_node.prev = before
		after.prev = new_node
		self.length += 1
		return True
	

	def remove(self, index):
		if index < 0 or index >= self.length:
			return None
		if index == 0:
			return self.pop_first()
		if index == self.length - 1:
			return self.pop()
		to_rmv = self.get(index)
		before = to_rmv.prev
		after = to_rmv.next
		before.next = after
		after.prev = before
		to_rmv.prev = None
		to_rmv.next = None
		self.length -= 1
		return to_rmv


my_dll = DoublyLinkedList(1)
my_dll.print_list()