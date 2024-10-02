# if you add an item to the tail of the linked list, it's O(1) => you need the address of tail, you know the tail, so you can add it directly
# if you delete an item from the tail of the linked list, it's O(n) => you need the address of the node before tail, you have to iterate through the list to find the pointer to the tail

# if you add an item to the head of the linked list, it's O(1) => you need the address of head, you know the head, so you can add it directly
# if you delete an item from the head of the linked list, it's O(1) => you need the address of head, you know the head, so you can delete it directly

# if you add an item to the middle of the linked list, it's O(n)
# if you delete an item from the middle of the linked list, it's O(n)

# lookup is O(n) => you have to iterate through the list to find the item
# indexing is O(n) => you have to iterate through the list to find the item
# BUT in list it is O(1) => you can directly access the item by index

# _________________ Linked List _________________ List
#  Append              O(1)                       O(1)
#  Prepend             O(1)                       O(n)
#  Pop                 O(n)                       O(1)
#  Pop first           O(1)                       O(n)
#  Lookup by index     O(n)                       O(1)
#  Lookup by value     O(n)                       O(n)
#  Insert              O(n)                       O(n)
#  Remove              O(n)                       O(n)

head = {
	"value": 10,
	"next": {
		"value": 5,
		"next": {
			"value": 16,
			"next": {
				"value": 22,
				"next": {
					"value": 30,
					"next": None
				}
			}
		}
	}
}

print(head["next"]["next"]["value"])

# 10 -> 5 -> 16 -> 22 -> 30 -> None

# self keyword says that it is a method in the class, not a standalone function

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

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.prepend(0)

my_linked_list.print_list()

print("popped")
my_linked_list.pop()
my_linked_list.print_list()

print("popped")
my_linked_list.pop()
my_linked_list.print_list()

print("popped")
my_linked_list.pop()
my_linked_list.print_list()

print("popped")
my_linked_list.pop()
my_linked_list.print_list()
	

def check(expect, actual, message):
	print(message)
	print("EXPECTED:", expect)
	print("RETURNED:", actual)
	print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Pop on linked list with one node -----\n")
linked_list = LinkedList(1)
linked_list.print_list()
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on linked list with multiple nodes -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()
popped_node = linked_list.pop()
check(3, popped_node.value, "Value of popped node:")
check(1, linked_list.head.value, "Head of linked list:")
check(2, linked_list.tail.value, "Tail of linked list:")
check(2, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on empty linked list -----\n")
linked_list = LinkedList(1)
linked_list.head = None
linked_list.tail = None
linked_list.length = 0
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop all -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.print_list()
popped_node = linked_list.pop()
check(2, popped_node.value, "Value of popped node (first pop):")
check(1, linked_list.head.value, "Head of linked list (after first pop):")
check(1, linked_list.tail.value, "Tail of linked list (after first pop):")
check(1, linked_list.length, "Length of linked list (after first pop):")
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node (second pop):")
check(None, linked_list.head, "Head of linked list (after second pop):")
check(None, linked_list.tail, "Tail of linked list (after second pop):")
check(0, linked_list.length, "Length of linked list (after second pop):")
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list (third pop):")
check(None, linked_list.head, "Head of linked list (after third pop):")
check(None, linked_list.tail, "Tail of linked list (after third pop):")
check(0, linked_list.length, "Length of linked list (after third pop):")

