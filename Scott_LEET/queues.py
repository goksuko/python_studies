class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		
class Queue:
	def __init__(self, value):
		new_node = Node(value)
		self.first = new_node
		self.last = new_node
		self.length = 1

	def enqueue(self, value):
		new_node = Node(value)
		if self.length == 0:
			self.first = new_node
			self.last = new_node
		else:
			self.last.next = new_node
			self.last = new_node
		self.length += 1
		return True
	
	def dequeue(self):
		if self.length == 0:
			return None
		temp = self.first
		if self.length == 1:
			self.first = None
			self.last = None
		else:
			self.first = temp.next
			temp.next = None
		self.length -= 1
		return temp





my_queue = Queue(4)

print('First:', my_queue.first.value)
print('Last:', my_queue.last.value)
print('Length:', my_queue.length)


"""
	EXPECTED OUTPUT:
	----------------
	First: 4
	Last: 4
	Length: 1

"""