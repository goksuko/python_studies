class Stack:
	def __init__(self):
		self.stack_list = []

	def print_stack(self):
		for i in range(len(self.stack_list)-1, -1, -1):
			print(self.stack_list[i])

	def is_empty(self):
		return len(self.stack_list) == 0

	def peek(self):
		if self.is_empty():
			return None
		else:
			return self.stack_list[-1]

	def size(self):
		return len(self.stack_list)

	def push(self, value):
		self.stack_list.append(value)

	def pop(self):
		length = len(self.stack_list)
		if length == 0:
			return
		else:
			return self.stack_list.pop()
		
def is_balanced_parentheses(str):
	my_stack = Stack()
	for char in str:
		if char == '(':
			my_stack.push(char)
		elif char == ')':
			popped = my_stack.pop()
			if popped != '(':
				return False
	return my_stack.is_empty()

# def is_balanced_parentheses(parentheses):
# 	stack = Stack()
# 	for p in parentheses:
# 		if p == '(':
# 			stack.push(p)
# 		elif p == ')':
# 			if stack.is_empty() or stack.pop() != '(':
# 				return False
# 	return stack.is_empty()


# def reverse_string(str):
# 	my_stack = Stack()
# 	new_string = ""
# 	old_string = ""
# 	for char in str:
# 		my_stack.stack_list.append(char)
# 	for char in my_stack.stack_list:
# 		new_string = char + old_string
# 		old_string = new_string
# 	return new_string

def reverse_string(string):
	stack = Stack()
	reversed_string = ""
 
	for char in string:
		stack.push(char)
 
	while not stack.is_empty():
		reversed_string += stack.pop()
 
	return reversed_string


def sort_stack(my_stack):
	if my_stack.is_empty():
		return None
	sorted_stack = Stack()
	while not my_stack.is_empty():
		temp = my_stack.pop()
		while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
			my_stack.push(sorted_stack.pop())

		sorted_stack.push(temp)
	while not sorted_stack.is_empty():
		my_stack.push(sorted_stack.pop())

